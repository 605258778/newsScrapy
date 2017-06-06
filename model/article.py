# -*- coding: utf-8 -*-
from sqlalchemy import Column, String , Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'tb_article'

    id = Column(Integer, primary_key=True)
    folder_id = Column(Integer)
    title = Column(String)
    content = Column(String)
    count_view = Column(Integer)
    count_comment = Column(Integer)
    type = Column(Integer)
    status = Column(String)
    is_comment = Column(Integer)
    is_recommend = Column(Integer)
    sort = Column(Integer)
    jump_url = Column(String)
    image_url = Column(String)
    image_net_url = Column(String)
    file_url = Column(String)
    file_name = Column(String)
    approve_status = Column(Integer)
    publish_time = Column(String)
    publish_user = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    update_time = Column(String)
    create_time = Column(String)
    create_id = Column(Integer)
    url = Column(String)
