from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Signature(BaseModel):
    signature:str
    type:str
    extended_type:str

class User(BaseModel):
    email:str
    username:str
    passwd:str
    image:str

# CREATE TABLE `user` (
#   `email` varchar(255) NOT NULL,
#   `username` varchar(255) NOT NULL,
#   `pass` varchar(255) NOT NULL,
#   `image` varchar(255) DEFAULT NULL,
#   PRIMARY KEY (`email`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

class Device(BaseModel):
    id:str
    dev_name:str
    dev_type:str
    last_scan:datetime
    join_in:datetime
    user:Optional[str] = None

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