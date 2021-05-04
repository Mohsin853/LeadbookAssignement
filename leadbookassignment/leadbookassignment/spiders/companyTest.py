# from scrapytest.tests import Type
# from ..items import LeadbookassignmentItem


# class TestPost(LeadbookassignmentItem):
#     # defining item that is being covered
#     item_cls = LeadbookassignmentItem

#     # defining field tests
#     company_name = Type(str)
#     source_url = Type(str)
    

#     # also supports methods!
#     def url_test(self, value: str):
#         if not value.startswith('http'):
#             return f'Invalid url: {value}'
#         return ''
