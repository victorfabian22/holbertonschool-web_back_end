#!/usr/bin/env python3
"""
Hypermedia pagination
"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(iself, page: int, page_size: int) -> Tuple:
        """Tuple"""
        a: int = (page * page_size) - page_size
        return (a, page_size * page)

    def dataset(self) -> List[List]:
        """
        Dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        that takes two integer arguments page with default
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        with open(self.DATA_FILE, "r") as f:
            reader = csv.reader(f)
            datos = list(reader)
            start, end = self.index_range(page, page_size)
            page_data = datos[start+1:end+1]
        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """dictionary"""
        content = self.get_page(page, page_size)
        with open(self.DATA_FILE, "r") as f:
            reader = csv.reader(f)
            datos = list(reader)
        total = len(self.dataset())
        rango = self.index_range(page, page_size)
        if rango[1] > total:
            nex_page = None
        else:
            nex_page = page + 1
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        my_dict = {
                    "page_size": len(content),
                    "page": page,
                    "data": content,
                    "next_page": nex_page,
                    "prev_page": prev_page,
                    "total_pages": math.ceil(total / page_size)
                    }
        return my_dict
