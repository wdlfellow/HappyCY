# Create your views here.
from django.shortcuts import render_to_response
from cy.models import User,Knowledge,KnowledgePoint,KnowledgeTestRecord
from datetime import *
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect


def index(request):
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username,password=password)
        if user != None:
            request.session['user_id'] = user[0].id
            knowledges = Knowledge.objects.all()
            return render_to_response("knowledgelist.html",{'knowledges': knowledges},context_instance = RequestContext(request))
        else:
            return render_to_response("index.html",{},context_instance = RequestContext(request))
    else:
        return render_to_response('index.html', {},context_instance = RequestContext(request))

def register(request):
    if 'inputEmail3' in request.POST:
        username = request.POST['inputEmail3']
        password = request.POST['inputPassword3']
        passwordConfirm = request.POST['inputPassword33']
        email = request.POST['inputEmail3']

        user = User(username=username,password=password, email=email)
        user.save()
        return render_to_response('regsuccess.html',context_instance = RequestContext(request))
    else:
        return render_to_response('register.html',context_instance = RequestContext(request))

def kptest(request, offset):
    userid = request.session['user_id']
    knowledgeid = int(offset)

    allkppoints = KnowledgePoint.objects.all()
    startkgpoint = allkppoints[0]

    kgtestrecord = KnowledgeTestRecord.objects.filter(knowledgeid=knowledgeid, userid=userid)
    currentkgtid = 0
    if kgtestrecord != None and len(kgtestrecord) > 0:
        currentkgtid = kgtestrecord[0].currentkgpid
        request.session['currentkgid'] = knowledgeid
    return render_to_response('knowledgetest.html',{'currentkgtid':currentkgtid, 'startkgpoint':startkgpoint})

def submitanswer(request):
    userid = request.session['user_id']
    currentkgpid = request.POST['currentkgpid']
    currentkgid = request.session['currentkgid']
    record = KnowledgeTestRecord(userid=userid,currentkgpid = int(currentkgpid),finished=False, knowledgeid=currentkgid)
    record.save()

    return render_to_response('',{}) #saved and do the next test
