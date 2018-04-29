from django.http import HttpResponse

# Create your views here.
from LaoKimHengApp.models import UserAccount

print("Begin Application")

def adduser(request):
    sample = UserAccount(id="1", username="ttungmayy", password="12345")
    sample.save()
    return HttpResponse("Successful")

def show(request):
    sample = UserAccount.objects.get(pk = "1")
    return HttpResponse(sample.password)

def showall(request):
    sampleset = UserAccount.objects.all()
    len(sampleset) == 0
    for i in sampleset:
        print(i.username)
    return HttpResponse("See your console")


