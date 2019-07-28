#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import inspect

from common import session
from common import hlog
from model import Films


def get_films():
    """
    获取电影信息
    :return:
    """

    from utils import get_urls

    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)

    film_list = list()
    film_objs = session.query(Films).all()

    for obj in film_objs:
        hlog.info("开始读取从数据查询到的电影记录。")

        film_id = obj.id
        hlog.var('film_id', film_id)

        location_list = get_urls('Location', film_id)
        people_list = get_urls('People', film_id)
        specie_list = get_urls('Specie', film_id)
        vehicle_list = get_urls('Vehicle', film_id)

        film = {
            "id": obj.id,
            "title": obj.title,
            "description": obj.description,
            "director": obj.director,
            "producer": obj.producer,
            "release_date": obj.release_date,
            "rt_score": obj.rt_score,
            "url": obj.url,
            "people": people_list,
            "species": specie_list,
            "locations": location_list,
            "vehicles": vehicle_list
        }

        film_list.append(film)

    hlog.info("读取电影信息成功。")

    hlog.exit_func(func_name)

    return film_list
