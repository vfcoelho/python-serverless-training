
class TestBase(object):

    def test_base(self):

        from functions.wishlist_handler import claim_gift

        # event = {'body':'{"id":1}'}
        event = {'body':'{"id":1}','requestContext':{'stage':'local'}}

        claim_gift(event,None)