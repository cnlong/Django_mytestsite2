from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
# request 是HttpRequest类型的对象
# request包含浏览器请求的信息


def index(request):
    return render(request, 'booktest/index.html')


def show_arg(request, bid):
    return HttpResponse(bid)


# 自定义错误页面的视图函数
def bad_request(request, exception):
    return render(request, '400.html', status=400)


def permission_denied(request, exception):
    return render(request, '403.html', status=403)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def error(request):
    return render(request, '500.html')


def login(request):
    """显示登录页面"""
    # 判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已登录，跳转到首页
        return redirect('/index')
    else:
        # 用户未登录
        # 判断是否有cookie。从cookie中获取已输入的用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'booktest/login.html', {'username': username})


def login_check(request):
    """登录校验视图"""
    # request.POST 保存的是post方式提交的参数,QueryDict类型数据，类似于字典
    # request.GET 保存的是get方式提交的参数
    # 1.获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 获取记住按钮的值
    remember = request.POST.get('remember')
    # 2.进行登录校验
    # 实际开发：使用用户名和密码查找数据库
    # 模拟admin 123
    if username == 'admin' and password == '123':
        response = redirect('/index')
        # 用户名密码正确
        # 跳转到首页
        # 判断记住按钮的值
        if remember == 'on':
            # 设置cookie(username)，过期时间为1周
            response.set_cookie('username', username, max_age=7*24*3600)
        # 记住用户的登录状态
        # 只有session中有islogin，就认为该用户已经登录
        request.session['islogin'] = True
        return response  # redirect('/index')返回发就是一个HttpResponseRedirect对象，就是HttpResponse的子类
    else:
        # 用户名密码错误
        return redirect('/login')


def ajax_test(request):
    """显示ajax页面"""
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    """ajax请求处理"""
    # 返回的json数据 {'res': 1}，json格式返回数据
    return JsonResponse({'res': 1})


def login_ajax(request):
    """显示ajax登录页面"""
    return render(request, 'booktest/login_ajax.html')


def login_ajax_check(request):
    """ajax登录校验视图"""
    # 1.获取用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 2.进行登录校验
    # 实际开发：使用用户名和密码查找数据库
    # 模拟admin 123
    if username == 'admin' and password == '123':
        # 用户名密码正确
        # 跳转到首页
        # ajax的请求在后台处理，必须返回Json数据，不要返回页面或者重定向
        # return redirect('/index')
        return JsonResponse({'res': 1})
    else:
        # 用户名密码错误
        return JsonResponse({'res': 0})


def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse('设置cookie')
    # 设置cookie信息，键值对,可以通过max_age=（秒数）, expires=（时间，可以当前时间的14天之后的时间） 两个选项设置过期时间
    response.set_cookie('num', 1)
    return response


def get_cookie(request):
    """获取cookie信息"""
    # 取出cookie中num的值,COOKIES是一个字典
    num = request.COOKIES['num']
    return HttpResponse(num)


def set_session(request):
    """设置session"""
    request.session['username'] = 'smart'
    request.session['age'] = 18
    return HttpResponse('设置session')


def get_session(request):
    """获取session"""
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+":"+str(age))


def clear_session(request):
    """清除session的信息"""
    request.session.clear()
    return HttpResponse('清除成功')