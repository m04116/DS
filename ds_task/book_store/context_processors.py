from datetime import datetime


def copyright(request):
    # copyright = 'CopyRight - 2017'
    copyright_current_year = datetime.now().year
    copyright_start_year = '(C) 2016 - '
    # return locals()
    context = {'copyright_start_year': copyright_start_year,
               'copyright_current_year': copyright_current_year}
    return context
