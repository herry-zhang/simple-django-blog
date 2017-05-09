from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_page(request, post, limit=5):
    paginator = Paginator(post, limit)
    _page_num = paginator.num_pages
    _page = request.GET.get('p')
    if not _page:
        _page = 1
    try:
        _page = int(_page)
    except ValueError:
        _page = 1

    first_page = None
    last_page = None
    if _page_num <= 9:
        page_num = range(1, _page_num + 1)
    elif _page <= 5:
        page_num = range(1, 10)
    elif _page > 5 & _page < _page_num - 3:
        page_num = range(_page - 4, _page + 5)
        first_page = 1
        last_page = _page_num
    else:
        page_num = range(_page_num - 8, _page_num + 1)

    try:
        post_list = paginator.page(_page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(_page_num)

    return {'post_list': post_list, 'page_num': page_num, 'page': _page,
            'first_page': first_page,
            'last_page': last_page, 'current_page': _page}
