from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def depart_list(request):
    queryset = models.Department.objects.all()

    return render(request, "depart_list.html", {"Queryset": queryset})


def depart_add(request):
    if request.method == "GET":
        return render(request, "depart_add.html")

    title = request.POST.get("title")
    models.Department.objects.create(title=title)

    return redirect("/depart/list/")


def depart_delete(request):
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()

    return redirect("/depart/list/")


def depart_edit(request, nid):
    if request.method == "GET":
        row_obj = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"departname": row_obj})

    newname = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=newname)
    return redirect("/depart/list/")


def user_list(request):
    queryset = models.UserInfo.objects.all()
    # for obj in queryset:
    #     print(obj.id,obj.name,obj.start_time.strftime("%Y-%M-%D"),obj.get_gender_display(),obj.depart.title)

    return render(request, "user_list.html", {"queryset": queryset})


def user_add(request):
    context = {
        'genderchoice': models.UserInfo.gender_choices,
        'departdata': models.Department.objects.all()
    }
    return render(request, "user_add.html", context)


from django import forms


class usermodel(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "start_time", "depart", "gender"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def modelform_user_add(request):
    if request.method == "GET":
        userform = usermodel(),
        return render(request, "modelform_user_add.html", {"userform": userform})

    userform = usermodel(data=request.POST)
    if userform.is_valid():
        userform.save()
        return redirect("/user/list/")

    return render(request, "modelform_user_add.html", {"userform": userform})


def user_edit(request, nid):
    rawdata = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        userform = usermodel(instance=rawdata)
        return render(request, "user_edit.html", {"userform": userform})

    if request.method == "POST":

        userform = usermodel(data=request.POST, instance=rawdata)
        if userform.is_valid():
            userform.save()
            return redirect("/user/list/")
        return render(request, "user_edit.html", {"userform": userform})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


from django.core.exceptions import ValidationError

class nummodel(forms.ModelForm):
    class Meta:
        model = models.SuperNum
        # fields = ["mobile", "price", "level", "status"]
        # exclude["status"]
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_mobile(self):

        text_mobile = self.cleaned_data["mobile"]
        exist = models.SuperNum.objects.filter(mobile=text_mobile).exists()
        if exist:
            raise ValidationError("Already Exist")
        return text_mobile


def num_list(request):
    """Sort by level in reverse order"""
    queryset = models.SuperNum.objects.all().order_by("-level")
    # for obj in queryset:
    #     print(obj.id,obj.name,obj.start_time.strftime("%Y-%M-%D"),obj.get_gender_display(),obj.depart.title)

    return render(request, "num_list.html", {"queryset": queryset})


def num_add(request):
    if request.method == "GET":
        numform = nummodel()
        return render(request, "num_add.html", {"numform": numform})

    numform = nummodel(data=request.POST)
    if numform.is_valid():
        numform.save()
        return redirect("/num/list/")
    return render(request, "num_add.html", {"numform": numform})



class editnummodel(forms.ModelForm):
    class Meta:
        model = models.SuperNum
        # fields = ["mobile", "price", "level", "status"]
        # exclude["status"]
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_mobile(self):

        text_mobile = self.cleaned_data["mobile"]
        exist = models.SuperNum.objects.exclude(id=self.instance.pk).filter(mobile=text_mobile).exists()
        if exist:
            raise ValidationError("Already Exist")
        return text_mobile


def num_edit(request,nid):
    rawdata = models.SuperNum.objects.filter(id=nid).first()
    if request.method == "GET":
        numform = editnummodel(instance=rawdata)
        return render(request,"num_edit.html",{"numform":numform})

    numform = editnummodel(data=request.POST,instance=rawdata)
    if numform.is_valid():
        numform.save()
        return redirect("/num/list/")
    return render(request, "num_edit.html", {"numform": numform})

def num_delete(request,nid):
    models.SuperNum.objects.filter(id=nid).delete()
    return redirect("/num/list/")
