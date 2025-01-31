from app.database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, Boolean, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="user"
    email = Column(VARCHAR(255), primary_key=True)
    username = Column(VARCHAR(255), unique=True)
    passwd = Column("passwd",VARCHAR(255))
    image = Column(VARCHAR(255))

# CREATE TABLE `user` (
#   `email` varchar(255) NOT NULL,
#   `username` varchar(255) NOT NULL,
#   `pass` varchar(255) NOT NULL,
#   `image` varchar(255) DEFAULT NULL,
#   PRIMARY KEY (`email`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

class Device(Base):
    __tablename__="device"
    id = Column(VARCHAR(255), primary_key=True)
    dev_name = Column(VARCHAR(255))
    dev_type = Column(VARCHAR(255))
    last_scan = Column(DateTime)
    join_in = Column(DateTime)
    user = Column(VARCHAR(255), ForeignKey("user.email"))

# CREATE TABLE `device` (
#   `id` varchar(255) NOT NULL,
#   `dev_name` varchar(255) DEFAULT NULL,
#   `dev_type` varchar(255) DEFAULT NULL,
#   `last_scan` datetime DEFAULT NULL,
#   `join_in` datetime DEFAULT NULL,
#   `user` varchar(255) DEFAULT NULL,
#   PRIMARY KEY (`id`),
#   KEY `user` (`user`),
#   CONSTRAINT `device_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`email`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

class Signature(Base):
    __tablename__="signature"
    signature = Column(VARCHAR(255), primary_key=True)
    type = Column(VARCHAR(255))
    extended_type = Column(VARCHAR(255))