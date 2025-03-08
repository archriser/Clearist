# Clyde - CLI todolist for developers. Minimal and no BS
A simple, terminal-based to-do list for developers. Minimal, fast, and secure.  
Syncs with Nextcloud, Google Drive, and GitHub. Encrypts tasks before storage.  
No bloat. Just a to-do list that works.  


# Clyde Development To-Do List

## **Phase 1: Core Functionality (Local Storage & Task Management)**
- [ ] Set up the project folder structure.  
- [ ] Implement a CLI interface (`cli.py`) to handle user input.  
- [ ] Create a `tasks.py` module for adding, removing, updating, and listing tasks.  
- [ ] Implement a secure local storage system:  
  - Choose **SQLite (SQLCipher)** or **AES-encrypted JSON**.  
  - Encrypt before saving, decrypt only when needed.  
- [ ] Implement task categories, priorities, and due dates.  

## **Phase 2: Sync Features**
- [ ] Implement **Nextcloud Sync** (via WebDAV).  
  - Authenticate using OAuth or API tokens.  
  - Encrypt data before uploading.  
- [ ] Implement **Google Drive Sync**.  
  - Authenticate using OAuth 2.0.  
  - Upload encrypted task files as a backup.  
- [ ] Implement **GitHub Sync** (private repo backup).  
  - Store encrypted backups in a private GitHub repository.  
  - Automate commits & pushes.  

## **Phase 3: Backup & Export**
- [ ] Implement **manual and automatic backups**:  
  - Export tasks as **JSON, CSV, or SQLite dumps**.  
  - Allow users to schedule automatic backups.  
- [ ] Add an option to **restore from backups**.  

## **Phase 4: Optimization & Additional Features**
- [ ] Optimize CLI performance and error handling.  
- [ ] Secure authentication (e.g., store API keys safely).  
- [ ] Add a configuration system (`config.py`) for custom settings.  
- [ ] Write tests (`tests/`) for storage, sync, and task management.  
- [ ] Write documentation (`README.md`, `usage.md`).  

