from .models import company



def get_company_info(request):
    campany = company.objects.last()
    return {'info':campany}
    