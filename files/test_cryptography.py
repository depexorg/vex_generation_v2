import subprocess
import tempfile
import os
from cryptography import __version__ as crypto_version
from cryptography.hazmat.primitives.serialization import load_ssh_public_identity

def is_option_malformed(value: bytes) -> bool:
    # Example: detects length prefixes encoded in the first 4 bytes
    return value.startswith(b"\x00\x00") or len(value) > 0 and value[0] < 32

print(f"🔐 Detected cryptography version: {crypto_version}\n")

with tempfile.TemporaryDirectory() as tmpdir:
    ca_key = os.path.join(tmpdir, "ca")
    user_key = os.path.join(tmpdir, "user")
    cert_file = user_key + "-cert.pub"

    subprocess.run(["ssh-keygen", "-f", ca_key, "-N", ""], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["ssh-keygen", "-f", user_key, "-N", ""], check=True, stdout=subprocess.DEVNULL)
    subprocess.run([
        "ssh-keygen", "-s", ca_key, "-I", "test", "-n", "testuser",
        "-O", "critical:force-command=echo hello_from_cert"
    ] + [user_key + ".pub"], check=True, stdout=subprocess.DEVNULL)

    with open(cert_file, "rb") as f:
        cert_data = f.read()

    cert = load_ssh_public_identity(cert_data)
    print("🟡 Certificate loaded successfully.")

    if any(is_option_malformed(v) for v in cert.critical_options.values()):
        print("⚠️  Critical options appear malformed:")
        for k, v in cert.critical_options.items():
            print(f"  - {k!r}: {v!r}")
        print("🔴 This version is VULNERABLE to CVE-2023-38325 (critical options misdecoded).")

    else:
        print("✅ Critical options successfully exposed:")
        for k, v in cert.critical_options.items():
            print(f"  - {k!r}: {v.decode(errors='replace')}")
        print("🟢 This version is SAFE (vulnerability patched).")
