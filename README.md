# Molecule Example

Required: python3, Docker
Vault password: somepass

#### Local run
  
  1. Create and activate virtualenv

  ```bash
  python3 -m venv .venv
  source ./.venv/bin/activate
  ```

  2. Install dependencies

  ```bash
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
  ```

  3. Export ANSIBLE_VAULT_PASSWORD_FILE environment variable

  ```bash
  export ANSIBLE_VAULT_PASSWORD_FILE=<file>
  ```

  4. Run molecule test

  ```
  cd roles/config_vm
  molecule test
  ```
  
