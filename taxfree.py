from algoliasearch.search_client import SearchClient


class TaxFree:

    def __init__(self):
        appid = ''
        apikey = ''

        self.client = SearchClient.create(appid, apikey)
        self.index = self.client.init_index('products')

    def search(self, search_string, category, sub_category=None, sub_sub_category=None):
        # Search without sub-category is a bad idea, as the max returned search items is 1k

        page = 0
        hits = []

        if sub_sub_category is not None:
            category_filter = 'categoryPathHierarchy.lvl1:"{} > {} > {}"'.format(category.capitalize(),
                                                                                 sub_category.capitalize(),
                                                                                 sub_sub_category.capitalize())
        elif sub_category is not None:
            category_filter = 'categoryPathHierarchy.lvl1:"{} > {}"'.format(category.capitalize(),
                                                                            sub_category.capitalize())
        else:
            category_filter = 'categoryPathHierarchy.lvl0:{}'.format(category.capitalize())

        while True:
            result = self.index.search(search_string,
                                       {
                                           'filters': category_filter,
                                           'hitsPerPage': 100,
                                           'page': page
                                       })
            hits.extend(result['hits'])
            total_pages = result['nbPages']
            page = result['page'] + 1

            if page > total_pages:
                return hits

    def browse(self, category):
        # Browse needs to be allowed by the api key
        search_category = category.capitalize()
        result = self.index.browse_objects(
            {
                'filters': 'categoryPathHierarchy.lvl0:{}'.format(search_category),
                'query': '',
            })
        return result


