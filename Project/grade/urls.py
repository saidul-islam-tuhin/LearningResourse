from django.conf.urls import url
from . import views


urlpatterns = [
    #/grade/result/
    #url(r'^result/$', views.result, name='result'),
    #grade/result/std_id
    #url(r'^result/(?P<student_id>[0-9]+)$', views.details, name='details'),
    url('^web_scraping/$', views.web_scraping, name='web_scraping'),
    url('^ajax/$', views.input_json, name='input_json'),
    url('^ajax/json/$', views.test_json, name='test_json'),
    url('^ajax/result/$', views.result_ajax, name='result_ajax'),
    url('^signup/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^signup/ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^show/(?P<one>[a-zA-Z]+)/(?P<two>[0-9]+)/', views.show, name="show"),
    url(r'^questions/(?P<pk>\w+)/$', views.question_details, name='question_details'),

]