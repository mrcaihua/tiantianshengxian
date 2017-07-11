class urlMiddleware:
    def process_view(self,request,view_name,view_args,view_kwargs):
        if request.path not in['/ttsx_user/register/',
                               '/ttsx_user/register_handle/',
                               '/ttsx_user/register_valid/',
                               '/ttsx_user/login/',
                               '/ttsx_user/login_handle/',
                               '/ttsx_user/logout/',
                               '/ttsx_user/login/',]:
            request.session['url_path']=request.get_full_path()


