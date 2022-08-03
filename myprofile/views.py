from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Content, SubWork, Work
from .Form.contactForm import ContactForm
# Create your views here.


def Index(request):
    about_sites = Content.objects.filter(contents_type="SITE").first()
    about_me = Content.objects.filter(contents_type="PROFILE").first()
    skills = Content.objects.filter(contents_type="SKILLS").first()
    skill_db = skills.related_content.filter(type="DB").order_by("name")
    skill_language = skills.related_content.filter(type="Language").order_by("name")
    skill_framework = skills.related_content.filter(type="Framework").order_by("name")
    works = Content.objects.filter(contents_type="WORKS").first()
    work_contents = works.work_content.all()
    template = loader.get_template('myprofile/index.html')

    # 問い合わせフォーム
    contact_form = ContactForm()
    isSuccess = False
    if request.method == "POST":
        contact_form = RegisterContact(request)

    # 水玉用
    for_range_li = [i for i in range(15)]

    # テーブルのレイアウトをそろえる用の変数
    skill_max_count = max([len(skill_db), len(skill_language), len(skill_framework)])
    for_range_skill_db = [i for i in range(skill_max_count - len(skill_db))]
    for_range_skill_language = [i for i in range(skill_max_count - len(skill_language))]
    for_range_skill_framework = [i for i in range(skill_max_count - len(skill_framework))]

    context = {
        'about_sites': about_sites,
        'about_me': about_me,
        'skills': skills,
        'skill_db': skill_db,
        'skill_language': skill_language,
        'skill_framework': skill_framework,
        'works': works,
        'work_contents': work_contents,
        'for_range_skill_db': for_range_skill_db,
        'for_range_skill_language': for_range_skill_language,
        'for_range_skill_framework': for_range_skill_framework,
        'for_range_li': for_range_li,
        'contact_form': contact_form,
        'isSuccess': isSuccess,
    }
    return HttpResponse(template.render(context, request))


def WorkDetail(request, work_id):
    if request.method == 'GET':
        work = Work.objects.filter(pk=work_id)
        work_detail = SubWork.objects.filter(work_id=work[0].pk)
        img_url_root = work[0].top_image.url[:work[0].top_image.url.find("/", 1) + 1]
        work = list(work.values())
        work_detail = list(work_detail.values())
        context = {
            'work': work[0],
            'img_url_root': img_url_root,
            'work_detail': work_detail[0],
        }
        return JsonResponse(context)


def RegisterContact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            post = contact_form.save()
            post.author = request.user
            post.save()
            contact_form.SendContactMail()
            return ContactForm()
    return contact_form
