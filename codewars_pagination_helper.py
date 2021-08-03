"""
For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class,
which is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each
page. The types of values contained within the collection/array are not relevant.

https://www.codewars.com/kata/515bb423de843ea99400000a/train/python
"""


class PaginationHelper:
    __slots__ = ['mycollection', 'itemspp']

    def __init__(self, collection, items_per_page):
        items_per_page = int(items_per_page)
        self.mycollection = collection
        self.itemspp = items_per_page

    def item_count(self):
        return len(self.mycollection)

    def page_count(self):
        return self.item_count() // self.itemspp + 1

    def page_item_count(self, ppage_index):
        ppage_index = int(ppage_index)
        pc = self.page_count() - 1

        if pc < ppage_index:
            return -1

        if pc - 1 >= ppage_index:
            return self.itemspp
        else:
            return divmod(self.item_count(), self.itemspp)[1]

    def page_index(self, item_index):
        item_index = int(item_index)
        if item_index < 0 or item_index >= self.item_count():
            return -1
        return item_index // self.itemspp
