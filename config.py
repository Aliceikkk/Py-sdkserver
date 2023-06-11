{
  "app": {
    "listen": "0.0.0.0",
    "port": 80,
    "debug": false,
    "secret_key": "FlaskVeryLowPasswordHere"
  },
  
  "mail": {
    "smtp_server": "your-smtp-server",
    "smtp_port": 465,
    "sender_email": "your-email-address",
    "sender_password": "your-email-password"
  },
  
  "dispatch": {
    "global": "http://192.168.160.135:21041",
    "local": {
      "dev_gio": "http://192.168.160.135:21041"
    }
  },
  "crypto": {
    "rsa": {
      "password": "-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDJ4Xyfdf5WTAiEB0Qroyn1kYxbfs320tYCVGcuRD/tdxwLt+Kb\nQu0rgWoRkuCdG+g+PSRYSGLqVaJjy/aA92QpeEurJO78JzZSD4t63tT23oTPeAh2\n3ebmnj32ZtEWHHxm69lvpD0jj75RdhYR82KxYAMY4GXmokPbcWcxxPOOKwIDAQAB\nAoGAU9oRnlYvJv77xoMSIKHr6rDiwJohyHR4KY2PMdttRh/kCUX+nIim5Bwjx1rf\nasJNq5RPxU+DrluVUKhGIfkfo5EKpxm7LIdO4EeTV0OD2xMABz3s0YOGW0lboc3Q\nYpJLeBh7fd+1O+OMJis2tVrcNXsLPODr5xVIOTXi0s9S2fkCQQDocZpH2VJ37Mu/\nCr7PU4/yCHPHOLDAqM181p0ULnEMuETW2H8hNOlE5h1yg/2YVS32afbGYCGWku66\nV64vEY1fAkEA3lb5o+l8yHf6Nhk9U6sO9v1ZGtjJ5qj5BEwrGtiV24YUG38lA+t7\nX6M2Is3bzRFUDvXQuRU9dY4CsT+QgYGmtQJBAN4rNvtVjK1zd4qyCo6/n+YGjiLs\n3IRI059uwdR4TzWJKsLvSxPCLvPbvmmmHs1rHPNZdLVHTNNOvT7+b04tyKECQCUZ\n7l5jv+bT3nTYkVs82Cpu7EeGlWpgF+2XqDm6mocfQIu2E78rtFKpMYdtQphdo+E7\nM7Eu0iqjn99j9AEoWWECQQDl1VONUQSYgE+dCPJ8vVtuZW+Iwq6ls/M6TlOqD0v2\nfVeh0XudmRzF3JnKMq9qZz3m+CFQ0nMsUikaC36+wpJe\n-----END RSA PRIVATE KEY-----",
      "authkey": {
        "1": "-----BEGIN PUBLIC KEY-----\nMIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQB62b+/gK3AIdJA/Dti7lgC\n/PjaqWYAQwSZ8sMqT8m2ksOj/1p7vwEiN5aQnZZx03V0hVgxHtdr6q5NRZ7rOF6g\n5hn9OVbvMacMiqvUQr9tL0XF67EwIqaymsujkTyXwvpgLYvNHZ1YJbs3wcbg56Wj\nV7BuhPcsoFeXvpvlbTQvemr+jGIkr2qhfaa2k0IFPugiT4/7Zqroy1NECCroz0SV\neX8goiPeVMde7JHbCnZGN2ar1drHv3Jk7pPHiVMAgKk+JS5T7BU09qxX7HlhOzCw\nLD/d9fTP8lQdC+Rzd+KToKHeGed8/ZucnwKyB0C2C4k/wXg0FLezica4HRG/oFsb\nAgMBAAE=\n-----END PUBLIC KEY-----"
      }
    }
  },
  "security": {
    "bcrypt_cost": 12,
    "token_length": 32,
    "min_password_len": 8
  },
  "auth": {
    "enable_password_verify": false,
    "enable_server_guest": true
  }
}
