
CREATE DATABASE faq_system;
USE faq_system;

CREATE TABLE faqs(
id INT AUTO_INCREMENT PRIMARY KEY,
question TEXT,
answer TEXT,
rating INT DEFAULT 0
);
