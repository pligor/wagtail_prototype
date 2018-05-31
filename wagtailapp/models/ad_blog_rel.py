# from django.db import models
# #
# # class AdvertBlogPageIndexRelationship(models.Model):
# #     ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
# #     blog_page_ind = models.ForeignKey(BlogIndexPageModel, on_delete=models.CASCADE)
# #     # time_elapsed_per_dev = models.IntegerField(verbose_name="Time elapsed", null=True,
# #     #                                            default=None, blank=True)
#
# class AdvertBlogPageIndexRelationship(models.Model):
#     from .advert_snippet import Advert
#     ad = models.ForeignKey(Advert, on_delete=models.CASCADE)
#
#     from .blog_index_page import BlogIndexPage
#     blog_page_ind = models.ForeignKey(BlogIndexPage, on_delete=models.CASCADE)
#     # time_elapsed_per_dev = models.IntegerField(verbose_name="Time elapsed", null=True,
#     #                                            default=None, blank=True)
