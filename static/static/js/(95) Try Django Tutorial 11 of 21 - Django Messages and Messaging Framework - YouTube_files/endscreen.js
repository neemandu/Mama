(function(g){var window=this;var QAa=function(a,b,c,d){var e=b.Ub();g.R(a.element,"ytp-suggestion-set",!!e.videoId);var f=b.getPlaylistId();d=b.Xc(c,d?d:"mqdefault.jpg");var k=b instanceof g.hO?g.FV(b.lengthSeconds):null,l=!!f;f=l&&"RD"==(new g.GQ(f.substr(0,2),f.substr(2))).type;var m=b instanceof g.hO?b.ua:null;c={title:b.title,author:b.author,author_and_views:e.shortViewCount?b.author+" \u2022 "+e.shortViewCount:b.author,aria_label:b.pk||g.T("YTP_WATCH_VIDEO_OR_PLAYLIST",{TITLE:b.title},b.title),duration:k,url:b.Nk(c),is_live:m,
is_list:l,is_mix:f,background:d?"background-image: url("+d+")":""};b instanceof g.IQ&&(c.playlist_length=b.getLength());a.update(c)},C5=function(a,b){g.IH.call(this,{G:"div",
ba:["html5-endscreen","ytp-player-content",b||"base-endscreen"]});this.o=a;this.created=!1},D5=function(a){var b={G:"span",
M:"ytp-upnext-top",J:[{G:"span",M:"ytp-upnext-header",J:[g.T("YTP_PLAYLIST_UP_NEXT")]},{G:"span",M:"ytp-upnext-title",J:["{{title}}"]},{G:"span",M:"ytp-upnext-author",J:["{{author}}"]}]},c={role:"button",href:"{{url}}","aria-label":g.T("YTP_AUTOPLAY_NEXT")};b={G:"div",M:"ytp-upnext",P:{"aria-label":"{{aria_label}}"},J:[{G:"div",M:"ytp-cued-thumbnail-overlay-image",P:{style:"{{background}}"}},b,{G:"a",M:"ytp-upnext-autoplay-icon",P:c,J:[{G:"svg",P:{height:"100%",version:"1.1",viewBox:"0 0 72 72",width:"100%"},
J:[{G:"circle",M:"ytp-svg-autoplay-circle",P:{cx:"36",cy:"36",fill:"#fff","fill-opacity":"0.3",r:"31.5"}},{G:"circle",M:"ytp-svg-autoplay-ring",P:{cx:"-36",cy:"36","fill-opacity":"0",r:"33.5",stroke:"#FFFFFF","stroke-dasharray":"211","stroke-dashoffset":"-211","stroke-width":"4",transform:"rotate(-90)"}},{G:"path",M:"ytp-svg-fill",P:{d:"M 24,48 41,36 24,24 V 48 z M 44,24 v 24 h 4 V 24 h -4 z"}}]}]},{G:"span",M:"ytp-upnext-bottom",J:[{G:"span",M:"ytp-upnext-cancel"},{G:"span",M:"ytp-upnext-paused",
J:[g.T("YTP_AUTOPLAY_PAUSED_3")]}]}]};g.U.call(this,b);this.B=null;b=this.g["ytp-upnext-cancel"];this.B=new g.U({G:"button",ba:["ytp-upnext-cancel-button","ytp-button"],P:{tabindex:"0","aria-label":g.T("YTP_AUTOPLAY_CANCEL")},J:[g.T("YTP_CANCEL")]});g.L(this,this.B);this.B.U("click",this.hP,this);this.B.ra(b);this.o=a;this.K=this.g["ytp-svg-autoplay-ring"];this.F=this.D=this.A=this.C=null;this.H=new g.iu(this.Vm,5E3,this);g.L(this,this.H);this.I=0;this.O(this.g["ytp-upnext-autoplay-icon"],"click",
this.qR);this.lB();this.O(a,"autonavvisibility",this.lB);this.O(a,"mdxnowautoplaying",this.FQ);this.O(a,"mdxautoplaycanceled",this.GQ);this.O(a,"mdxautoplayupnext",this.OD);3==this.o.Pa()&&(a=(a=g.LU(g.GU(this.o)))?a.fI():null)&&this.OD(a)},RAa=function(a,b){a.C=b;
QAa(a,b,g.X(a.o),"hqdefault.jpg")},E5=function(a,b){if(!a.A){g.mG("a11y-announce",g.T("YTP_PLAYLIST_UP_NEXT")+" "+a.C.title);
a.I=g.xG();a.A=new g.iu((0,g.z)(a.iq,a,b),25);a.iq(b);var c=b||g.X(a.o).experiments.l("autoplay_time")||1E4;a.o.sa("onAutonavCoundownStarted",c)}g.Bq(a.element,"ytp-upnext-autoplay-paused")},G5=function(a){F5(a);
a.I=g.xG();a.iq();g.Q(a.element,"ytp-upnext-autoplay-paused")},F5=function(a){a.A&&(a.A.dispose(),a.A=null)},H5=function(a,b){b=void 0===b?!1:b;
var c=g.X(a.o);if(c.experiments.g("autonav_notifications")&&b&&window.Notification&&window.document.hasFocus){var d=window.Notification.permission;"default"==d?window.Notification.requestPermission():"granted"!=d||window.document.hasFocus()||(d=a.C.Ub(),a.Vm(),a.D=new window.Notification(g.T("YTP_PLAYLIST_UP_NEXT"),{body:d.title,icon:d.Xc(c)}),a.F=a.O(a.D,"click",a.gR),a.H.start())}F5(a);a.o.Gj(!1,b)},SAa=function(a){C5.call(this,a,"subscribecard-endscreen");
var b=a.getVideoData();this.A=new g.U({G:"div",M:"ytp-subscribe-card",J:[{G:"img",M:"ytp-author-image",P:{src:b.profilePicture}},{G:"div",M:"ytp-subscribe-card-right",J:[{G:"div",M:"ytp-author-name",J:[b.author]},{G:"div",M:"html5-subscribe-button-container"}]}]});g.L(this,this.A);this.A.ra(this.element);this.B=new g.n_(g.T("YTP_SUBSCRIBE"),null,g.T("YTP_UNSUBSCRIBE"),null,!0,!1,b.Ql,b.subscribed,"trailer-endscreen",null,null,a);g.L(this,this.B);this.B.ra(this.A.g["html5-subscribe-button-container"]);
this.hide()},I5=function(a){var b=g.X(a),c=g.FI||g.ff?{style:"will-change: opacity"}:void 0,d=b.g&&!b.isDni,e=["ytp-videowall-still"];
b.l&&e.push("ytp-videowall-show-text");g.U.call(this,{G:"a",ba:e,P:{href:"{{url}}",target:d?"_blank":"","aria-label":"{{aria_label}}","data-is-live":"{{is_live}}","data-is-list":"{{is_list}}","data-is-mix":"{{is_mix}}"},J:[{G:"div",M:"ytp-videowall-still-image",P:{style:"{{background}}"}},{G:"span",M:"ytp-videowall-still-info",J:[{G:"span",M:"ytp-videowall-still-info-bg",J:[{G:"span",M:"ytp-videowall-still-info-content",P:c,J:[{G:"span",M:"ytp-videowall-still-info-title",J:["{{title}}"]},{G:"span",
M:"ytp-videowall-still-info-author",J:["{{author_and_views}}"]},{G:"span",M:"ytp-videowall-still-info-live",J:[g.T("YTP_LIVE")]},{G:"span",M:"ytp-videowall-still-info-duration",J:["{{duration}}"]}]}]}]},{G:"span",ba:["ytp-videowall-still-listlabel-regular","ytp-videowall-still-listlabel"],J:[{G:"span",M:"ytp-videowall-still-listlabel-icon"},g.T("YTP_PLAYLIST"),{G:"span",M:"ytp-videowall-still-listlabel-length",J:[" (",{G:"span",J:["{{playlist_length}}"]},")"]}]},{G:"span",ba:["ytp-videowall-still-listlabel-mix",
"ytp-videowall-still-listlabel"],J:[{G:"span",M:"ytp-videowall-still-listlabel-mix-icon"},g.T("YTP_MIX"),{G:"span",M:"ytp-videowall-still-listlabel-length",J:[" (50+)"]}]}]});this.B=d;this.A=a;this.o=null;this.U("click",this.C);this.U("keypress",this.D);g.X(a).L&&(a=a.app.da,b=this.element,g.Pa(a.g,b),g.Sa(a.g,b),c=String(a.F++),b.setAttribute("data-visual-id",c),g.af(this,(0,g.z)(a.D,a,b)))},J5=function(a){C5.call(this,a,"videowall-endscreen");
this.N=a;this.H=0;this.B=[];this.I=this.F=this.D=null;this.K=this.W=!1;this.C=new g.VF(this);g.L(this,this.C);this.L=new g.iu(g.Ea(g.Q,this.element,"ytp-show-tiles"),0);g.L(this,this.L);var b=new g.U({G:"button",ba:["ytp-button","ytp-endscreen-previous"],P:{"aria-label":g.T("YTP_PREVIOUS")},J:[g.xV()]});g.L(this,b);b.ra(this.element);b.U("click",this.dN,this);this.R=new g.CH({G:"div",M:"ytp-endscreen-content"});g.L(this,this.R);this.R.ra(this.element);b=new g.U({G:"button",ba:["ytp-button","ytp-endscreen-next"],
P:{"aria-label":g.T("YTP_NEXT")},J:[g.yV()]});g.L(this,b);b.ra(this.element);b.U("click",this.cN,this);this.A=new D5(a);g.L(this,this.A);g.eV(this.o,this.A.element,4);this.hide()},K5=function(a){return g.fV(a.o)&&a.mq()&&!a.I},TAa=function(a,b){return(0,g.G)(b.suggestions,function(b){b=g.mY(b);
g.L(a,b);return b})},L5=function(a){var b=a.qt();
b!=a.W&&(a.W=b,a.o.T("autonavvisibility"))},M5=function(a){g.kV.call(this,a);
g.iH({YTP_AUTOPLAY_CANCEL:"\u05d1\u05d8\u05dc \u05d4\u05e4\u05e2\u05dc\u05d4 \u05d0\u05d5\u05d8\u05d5\u05de\u05d8\u05d9\u05ea",YTP_AUTOPLAY_NEXT:"\u05d4\u05e4\u05e2\u05dc \u05d0\u05ea \u05d4\u05e1\u05e8\u05d8\u05d5\u05df \u05d4\u05d1\u05d0",YTP_AUTOPLAY_PAUSED_3:"\u05d4\u05d4\u05e4\u05e2\u05dc\u05d4 \u05d4\u05d0\u05d5\u05d8\u05d5\u05de\u05d8\u05d9\u05ea \u05de\u05d5\u05e9\u05d4\u05d9\u05ea",YTP_CANCEL:"\u05d1\u05d9\u05d8\u05d5\u05dc",YTP_MIX:"\u05de\u05d9\u05e7\u05e1",YTP_PLAYLIST_UP_NEXT:"\u05d4\u05e1\u05e8\u05d8\u05d5\u05df \u05d4\u05d1\u05d0",
YTP_UNSUBSCRIBE:"\u05d1\u05d9\u05d8\u05d5\u05dc \u05e8\u05d9\u05e9\u05d5\u05dd"});this.l=null;this.o=new g.VF(this);g.L(this,this.o);this.A=g.X(a);UAa(a)?this.l=new J5(this.g):this.A.aa?this.l=new SAa(this.g):this.l=new C5(this.g);g.L(this,this.l);g.eV(this.g,this.l.element,4);this.DC();this.o.O(a,"videodatachange",this.DC,this);this.o.O(a,"crn_endscreen",this.eL,this);this.o.O(a,"crx_endscreen",this.fL,this)},UAa=function(a){a=g.X(a);
return a.Kc&&!a.aa};
g.p(C5,g.IH);C5.prototype.create=function(){this.created=!0};
C5.prototype.destroy=function(){this.created=!1};
C5.prototype.mq=function(){return!1};
C5.prototype.qt=function(){return!1};g.p(D5,g.U);g.h=D5.prototype;g.h.Vm=function(){this.D&&(this.H.stop(),this.Aa(this.F),this.F=null,this.D.close(),this.D=null)};
g.h.lB=function(){g.HH(this,g.HU(this.o))};
g.h.gR=function(){window.focus();this.Vm()};
g.h.hide=function(){g.U.prototype.hide.call(this)};
g.h.iq=function(a){a=a||g.X(this.o).experiments.l("autoplay_time")||1E4;var b=Math.min(g.xG()-this.I,a);a=Math.min(b/a,1);this.K.setAttribute("stroke-dashoffset",-211*(a+1));1<=a&&3!=this.o.Pa()?H5(this,!0):this.A&&this.A.start()};
g.h.qR=function(a){!g.Rd(this.B.element,g.JF(a))&&g.iX(a,this.o)&&H5(this)};
g.h.hP=function(){g.JU(this.o,!0)};
g.h.FQ=function(a){this.o.Pa();this.show();E5(this,a)};
g.h.OD=function(a){this.o.Pa();this.C&&this.C.Ub().videoId==a.Ub().videoId||RAa(this,a)};
g.h.GQ=function(){this.o.Pa();F5(this);this.hide()};
g.h.V=function(){F5(this);this.Vm();g.U.prototype.V.call(this)};g.p(SAa,C5);g.p(I5,g.U);I5.prototype.Vj=function(){g.iV(this.A,this.element);var a=this.o.Ub().videoId,b=this.o.getPlaylistId();g.o0(this.A.app,a,this.o.Gd,b,void 0,void 0,void 0)};
I5.prototype.C=function(a){g.iX(a,this.A,this.B,this.o.Gd||void 0)&&this.Vj()};
I5.prototype.D=function(a){switch(a.keyCode){case 13:case 32:g.OF(a)||(this.Vj(),g.NF(a))}};g.p(J5,C5);g.h=J5.prototype;g.h.create=function(){C5.prototype.create.call(this);var a=this.o.getVideoData();a&&(this.D=TAa(this,a),this.F=a);this.ug();this.C.O(this.o,"appresize",this.ug);this.C.O(this.o,"onVideoAreaChange",this.ug);this.C.O(this.o,"videodatachange",this.eN);this.C.O(this.o,"autonavchange",this.lA);this.C.O(this.o,"autonavcancel",this.bN);this.C.O(this.element,"transitionend",this.HS)};
g.h.destroy=function(){g.XF(this.C);g.cf(this.B);this.B=[];this.D=null;C5.prototype.destroy.call(this);g.Bq(this.element,"ytp-show-tiles");this.L.stop()};
g.h.mq=function(){return 1!=this.F.autonavState};
g.h.show=function(){C5.prototype.show.call(this);g.Bq(this.element,"ytp-show-tiles");g.X(this.o).l?g.ku(this.L):this.L.start();(this.K||this.I&&this.I!=this.F.clientPlaybackNonce)&&g.JU(this.o,!1);var a=K5(this);g.fV(this.o)&&g.X(this.o).experiments.g("ui_logging")&&g.UU(this.o,"end",{cancelButtonShow:a?"1":"0",state:this.mq()?"enabled":"disabled"});a?(L5(this),2==this.F.autonavState?g.X(this.o).experiments.g("fast_autonav_in_background")&&3==this.o.pi()?H5(this.A,!0):E5(this.A):3==this.F.autonavState&&
G5(this.A)):(g.JU(this.o,!0),L5(this))};
g.h.hide=function(){C5.prototype.hide.call(this);G5(this.A);L5(this)};
g.h.HS=function(a){g.JF(a)==this.element&&this.ug()};
g.h.ug=function(){if(this.D&&this.D.length){g.Q(this.element,"ytp-endscreen-paginate");var a=g.XU(this.N,!0),b=g.VH(this.N);b&&(b=b.nd()?48:32,a.width-=2*b);var c=a.width/a.height,d=96/54,e=b=2,f=Math.max(a.width/96,2),k=Math.max(a.height/54,2),l=this.D.length,m=Math.pow(2,2);var n=l*m+(Math.pow(2,2)-m);n+=Math.pow(2,2)-m;for(n-=m;0<n&&(b<f||e<k);){var q=b/2,r=e/2,u=b<=f-2&&n>=r*m,D=e<=k-2&&n>=q*m;if((q+1)/r*d/c>c/(q/(r+1)*d)&&D)n-=q*m,e+=2;else if(u)n-=r*m,b+=2;else if(D)n-=q*m,e+=2;else break}d=
!1;n>=3*m&&6>=l*m-n&&(4<=e||4<=b)&&(d=!0);m=96*b;n=54*e;c=m/n<c?a.height/n:a.width/m;c=Math.min(c,2);m*=c;n*=c;m*=g.bd(a.width/m||1,1,1.21);n*=g.bd(a.height/n||1,1,1.21);m=Math.floor(Math.min(a.width,m));n=Math.floor(Math.min(a.height,n));a=this.R.element;g.Jh(a,m,n);g.rh(a,{marginLeft:m/-2+"px",marginTop:n/-2+"px"});RAa(this.A,this.D[0]);g.R(this.element,"ytp-endscreen-takeover",K5(this));L5(this);m+=4;n+=4;for(f=c=0;f<b;f++)for(k=0;k<e;k++)if(q=c,r=0,d&&f>=b-2&&k>=e-2?r=1:0==k%2&&0==f%2&&(2>k&&
2>f?0==k&&0==f&&(r=2):r=2),q=g.cd(q+this.H,l),0!=r){u=this.B[c];u||(u=new I5(this.o),this.B[c]=u,a.appendChild(u.element));D=Math.floor(n*k/e);var I=Math.floor(m*f/b),S=Math.floor(n*(k+r)/e)-D-4,Z=Math.floor(m*(f+r)/b)-I-4;g.yh(u.element,I,D);g.Jh(u.element,Z,S);g.rh(u.element,"transitionDelay",(k+f)/20+"s");g.R(u.element,"ytp-videowall-still-mini",1==r);g.R(u.element,"ytp-videowall-still-large",2<r);r=u;q=this.D[q];r.o!=q&&(r.o=q,QAa(r,q,g.X(r.A),g.zq(r.element,"ytp-videowall-still-large")?"hqdefault.jpg":
"mqdefault.jpg"),u=(q=q.Gd)&&q.itct)&&(q=r.A,g.X(q).L&&(q=q.app.da,r=r.element,D=r.getAttribute("data-visual-id"),g.Pa(q.g,r),g.gV(q,"onLogServerVeCreated",{id:D,tracking_params:u})));c++}g.R(this.element,"ytp-endscreen-paginate",c<l);for(b=this.B.length-1;b>=c;b--)e=this.B[b],g.Kd(e.element),g.bf(e);this.B.length=c}};
g.h.eN=function(){var a=this.o.getVideoData();this.F!=a&&(this.H=0,this.D=TAa(this,a),this.F=a,this.ug())};
g.h.cN=function(){this.H+=this.B.length;this.ug()};
g.h.dN=function(){this.H-=this.B.length;this.ug()};
g.h.kK=function(){return!!this.A.A};
g.h.lA=function(a){1==a?(this.K=!1,this.I=this.F.clientPlaybackNonce,F5(this.A),this.l&&this.ug()):(this.K=!0,this.l&&K5(this)&&(2==a?E5(this.A):3==a&&G5(this.A)))};
g.h.bN=function(a){if(a){for(a=0;a<this.B.length;a++)g.jV(this.N,this.B[a].element,!0);this.lA(1)}else this.I=null,this.K=!1;this.ug()};
g.h.qt=function(){return this.l&&K5(this)};g.p(M5,g.kV);g.h=M5.prototype;g.h.Kz=function(){var a=this.g.getVideoData(),b=!!(a&&a.suggestions&&a.suggestions.length);b=!UAa(this.g)||b;a=g.BO(a,"ypc_module");var c=g.p0(this.g.app);return b&&!a&&!c};
g.h.Jz=function(){return this.l.qt()};
g.h.gK=function(){return this.Jz()?this.l.kK():!1};
g.h.V=function(){g.cV(this.g,"endscreen");g.kV.prototype.V.call(this)};
g.h.load=function(){g.kV.prototype.load.call(this);this.l.show();g.X(this.g).aa&&.01>Math.random()&&g.UU(this.g,"end",{trailerEndscreenShow:1})};
g.h.unload=function(){g.kV.prototype.unload.call(this);this.l.hide();this.l.destroy()};
g.h.eL=function(a){this.Kz()&&(this.l.created||this.l.create(),"load"==a.ia&&this.load())};
g.h.fL=function(a){"load"==a.ia&&this.loaded&&this.unload()};
g.h.DC=function(){g.cV(this.g,"endscreen");var a=Math.max(1E3*(this.g.getVideoData().lengthSeconds-10),0);a=new g.DQ(a,0x8000000000000,{id:"preload",namespace:"endscreen"});g.L(this,a);var b=new g.DQ(0x8000000000000,0x8000000000000,{id:"load",priority:6,namespace:"endscreen"});g.L(this,b);g.$U(this.g,[a,b])};g.dY.endscreen=M5;})(_yt_player);