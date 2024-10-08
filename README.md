# Password Management System Description

This application is designed to securely store and manage the user's passwords. It implements advanced encryption to protect sensitive information, ensuring that only authorized individuals can access the stored data.

## How Does the Application Work?

### 1. **Login Screen**
When you open the application, the first thing you will see is a screen asking you to enter your master password. This is the primary key that protects all stored passwords.

### 2. **Password Management**
Once you enter the correct master password, you can safely view, add, or delete your passwords. Each time you add a new password, the application encrypts it before saving it in a special file called `data.enc`. This file is inaccessible without the master password.

### 3. **Master Password Creation**
If you're using the application for the first time, you can create a master password. This password is extremely important, as without it you will not be able to access the stored passwords. When creating it, the application allows you to save a security key (a `.key` file), which will be necessary to access the information later.

## Security System

### 1. **Data Encryption**
The true strength of the application's security lies in the encryption of the passwords. The application uses a strong encryption method called **Fernet**, which is part of the `cryptography` security library. This system converts passwords into an unreadable format for anyone without the correct key.

#### What Does This Mean?
- **Encryption**: When you store a password in the application, it is not saved as plain text. Instead, it is converted into a code that can only be decrypted with your master password.
- **Decryption**: When you need to view or copy a password, the application converts it back to its original format, but only if you have entered the correct master password.

### 2. **Additional Verification**
When performing critical operations, such as copying or deleting a password, the application will ask you to enter your operating system password. This adds an extra layer of security, preventing unauthorized individuals from manipulating the passwords if they gain access to the application.

- **On Windows**, the application verifies your password through system credentials.
- **On Linux/macOS**, a system called `PAM` is used to securely authenticate the user.

## Usage Process

1. **Login**: When you open the application, you are prompted to enter the master password. If it's your first time using the app, you will have the option to create one.
2. **Password Management**: After successful authentication, you can view, add, delete, or copy your passwords.
3. **Additional Verification**: To copy or delete a password, you will be prompted to enter your operating system password as an additional security measure.
4. **Encrypted Storage**: Passwords are stored in an encrypted manner and can only be decrypted with the correct key.

## Multi-language

To learn more, refer to the file [language.md](src/assets/lang/language.md).

## Dependencies
To install the necessary dependencies, run the following command in the terminal:
```sh
pip install -r requirements.txt
```

## Build
To build the application, if you are on Windows, you can run the `build.bat` file. If you are on Linux/macOS, you can run the `build.sh` file. This will generate a folder called `dist` with the compiled application.