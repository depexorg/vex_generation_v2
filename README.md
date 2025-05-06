# Vulnerability Exploitability eXchange Test

This repository contains two vulnerable code examples related to Software Supply Chain (SSC) libraries for Vulnerability Exploitability eXchange (VEX) generation. This document provides instructions to create a virtual environment using **pyenv**, and detailed descriptions about vulnerabilities identified in the Python libraries **cryptography (CVE-2023-38325)** and **PyYAML (CVE-2020-14343)**.

---

## 1. Creating a virtual environment with pyenv (Python 3.10.13)

### 📍 Installing pyenv

First, install `pyenv` following the instructions for your operating system:

- **macOS**:
  ```bash
  brew install pyenv
  ```

- **Linux (Ubuntu/Debian)**:
  ```bash
  curl https://pyenv.run | bash
  ```

Make sure to add the following lines to your `~/.bashrc` or `~/.zshrc` file:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

### 📍 Creating the virtual environment with Python 3.10.13

```bash
pyenv install 3.10.13
pyenv virtualenv 3.10.13 myenv
pyenv activate myenv
```

Now, your Python 3.10.13 virtual environment is active.

### 📍 Install Python libraries

```bash
pip install -r vulnerable_requirements.txt # For versions with vulnerabilites
pip install -r safe_requirements.txt # For versions without vulnerabilites
```

Finally, you can install vulnerable or safe dependencies to see demonstration scripts behaviour.

---

## 2. Vulnerability in cryptography library (CVE-2023-38325)

The provided code demonstrates a specific vulnerability **(CVE-2023-38325)** related to the incorrect handling of critical options in SSH certificates by the `cryptography` library. This vulnerability can lead to incorrect interpretation of critical options in signed certificates, potentially compromising security mechanisms. The specifically affected artifact is the function:

- `cryptography.hazmat.primitives.serialization.load_ssh_public_identity`

This function loads SSH certificates and is susceptible to malicious or incorrect decoding of certificate data. You can see if the version is vulnerable using the command:

```bash
python3 files/test_cryptography.py 
```

---

## 3. Vulnerability in PyYAML (CVE-2020-14343)

This example illustrates how PyYAML library can be exploited to execute arbitrary code when using the `yaml.full_load()` method with specially crafted YAML content. The identified vulnerability **(CVE-2020-14343)** allows an attacker to insert special tags into YAML loaded by PyYAML, resulting in remote execution of arbitrary commands.

The specifically affected artifact is:

- `yaml.full_load`

This function can load and execute arbitrary Python objects from malicious YAML data, significantly compromising system security. You can see if the version is vulnerable using the command:

```bash
python3 files/test_pyyaml.py 
```

---

## 📚 Final Notes

- Always review and regularly update dependencies to avoid known vulnerabilities.
- Use static analysis and automated auditing tools as [Depex](https://github.com/GermanMT/depex) to monitor software security.
- The SBOM files are used in [VEXGen](https://github.com/GermanMT/vexgen) to test the ability of generating Vulnerability Exploitabily eXchange (VEX) files.