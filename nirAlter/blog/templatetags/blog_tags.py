from django.template import loader, Library
from blog.models import *

register = Library()


@register.simple_tag(takes_context=True)
def recent_blog_posts(context, recents_name, template='blog/blog_recents_view.html'):
    request = context['request']
    recents_object = BlogRecentsSnippet.objects.get(title=recents_name)
    recents = BlogPage.objects.all()[:recents_object.display_count]

    print(recents[0])
    context.update({
        'recents_title': recents_object.title,
        'recent_blog_posts': recents,
    })

    return loader.get_template(template).render(context)
