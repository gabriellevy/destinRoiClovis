google.maps.__gjsload__('kml', function(_){var D9a=function(a){_.E(this,a,3)},E9a=function(a){_.E(this,a,3)},c9=function(a){_.E(this,a,1)},d9=function(a){_.E(this,a,2)},e9=function(a){_.E(this,a,2)},f9=function(a){_.E(this,a,2)},g9=function(a){_.E(this,a,2)},h9=function(a){_.E(this,a,2)},i9=function(a){_.E(this,a,4)},j9=function(a){_.E(this,a,6)},F9a=function(a){_.E(this,a,4)},k9=function(a){_.E(this,a,3)},l9=function(a){_.E(this,a,10)},m9=function(a){this.g=0;this.Nh=[];this.i=a},o9=function(){var a=this;this.ob=new _.ui(function(){var b=
G9a(a),c=a.get("projection");if(c&&_.Xe(b)){var d=a.get("mapBounds");if(d){var e=Math.pow(2,b),f=_.Ek(d);d=_.Dk(d);var g=f.lng(),h=d.lng();g>h&&(d=new _.rf(d.lat(),h+360,!0));f=c.fromLatLngToPoint(f);d=c.fromLatLngToPoint(d);f.x*=e;f.y*=e;d.x*=e;d.y*=e;e=new _.Vh([f,d]);e=_.Wh(e.hb,e.Wa,e.rb,e.mb);b=_.Yfa(c,b);c=(e.hb+e.rb)/2;b=c-_.Se(c,0,Math.sqrt(b.x*b.x+b.y*b.y));e.rb-=b;e.hb-=b;a.g&&_.xt(a.g,e)||(b=e.getCenter(),c=e.Pb(),a.g=new _.Vh([new _.M(b.x-c.width,b.y-c.height),new _.M(b.x+c.width,b.y+
c.height)]));n9(a)}}},0)},G9a=function(a){a=a.get("zoom");return _.Xe(a)?Math.round(a):a},n9=function(a){if(a.g){var b=a.g.getCenter(),c=a.get("projection");var d=a.get("bounds");var e=G9a(a);if(c&&d&&_.Xe(e)){d=_.Rl(c,d,e);if(b){var f=d.getCenter();(e=_.Sl(c,e))&&Infinity!=e&&0!=e&&(c&&c.getPov&&0!=c.getPov().heading()%180?(b=f.y-b.y,b=_.Se(b,-e/2,e/2)-b,d.Wa+=b,d.mb+=b):(b=f.x-b.x,b=_.Se(b,-e/2,e/2)-b,d.hb+=b,d.rb+=b))}d.hb-=_.Rj.width;d.Wa-=_.Rj.height;d.rb-=_.Rj.width;d.mb-=_.Rj.height}else d=
void 0;b=a.g;d=_.Wh(Math.max(b.hb,d.hb),Math.max(b.Wa,d.Wa),Math.min(b.rb,d.rb),Math.min(b.mb,d.mb));d.equals(a.i)||(a.set("croppedBounds",d),a.i=d)}},H9a=function(a,b){return{i:function(c){return"dragstart"!=c&&"drag"!=c&&"dragend"!=c},j:function(c,d){if(d)return null;var e=null,f=c.latLng;a.forEach(function(g){if(!e){var h=g.get("bounds");h&&h.contains(f)&&0!=g.get("clickable")&&(e=g)}});return e},handleEvent:function(c,d,e){"mouseover"==c?b.set("cursor","pointer"):"mouseout"==c&&b.set("cursor",
null);_.H.trigger(e,c,new _.zn(d.latLng,d.domEvent))},zIndex:10}},r9=function(a,b){var c=this;this.i=a;this.g=b;this.ob=new _.ui(function(){var d=c.get("projection"),e=c.get("bounds"),f=p9(c);I9a(c);if(d&&e&&_.Xe(f)&&!e.isEmpty()){var g=Math.round(e.Wa);e=Math.round(e.mb);d=c.get("projection");var h=p9(c),k=c.i;f=_.Ek(k).lng();var l=_.Dk(k).lng();h=_.Rl(d,k,h);h=Math.round(h.Pb().width);k=k.getNorthEast().lat()-k.getSouthWest().lat();for(var m=q9(c,g),p=g;g<=e;++g){var q=q9(c,g),r=p,t=g,v=m,w=q,x=
(v+w)/2,z=q9(c,(r+t)/2),J=Math.abs(g-p);if(1<=Math.abs((r-t)/(w-v)*(z-x))&&10<J||g==e)r=new _.rf(m,l),t=new _.rf(q,f),m=c,p=new _.Jg(h,g-p),t=new _.tg(t,r),v=k,r=d,w=_.Ek(t).lat(),x=_.Dk(t).lat(),x=p.height/(w-x),w=(_.Ek(m.i).lat()-w)*x,v=Math.abs(v*x),w=new _.M(0,w),x=_.Ek(t),p={Vw:w,position:x,Qq:p,scaledSize:new _.Jg(p.width,v)},v=t,t=_.Ek(v),v=_.Dk(v),w=t.lng(),x=v.lng(),w>x&&(v=new _.rf(v.lat(),x+360,!0)),r={min:_.Fl(t,r),max:_.Fl(v,r)},p.Gz=r,_.Ch(m.g,p),p=g,m=q}}_.Tt((0,_.Za)(c.j,c))()},0)},
p9=function(a){a=a.get("zoom");return _.Xe(a)?Math.round(a):a},I9a=function(a){a.g.forEach(function(b){b.hw=!0})},q9=function(a,b){var c=a.get("projection");a=p9(a);return _.Ql(c,new _.M(0,b),a).lat()},t9=function(a,b,c,d){var e=this;this.N=a;this.j=b;this.g=c;this.i=d;_.H.addListener(c,"insert",(0,_.Za)(this.O,this));_.H.addListener(c,"remove",(0,_.Za)(this.H,this));setTimeout(function(){if(e.g.Pb()){var f=s9(e);e.g.forEach((0,_.Za)(e.H,e));e.g.forEach((0,_.Za)(e.o,e,f))}},0)},s9=function(a){a=a.get("opacity");
return _.Ve(a,1)},u9=function(a){this.g=_.ik(_.fr,_.nj,a+"/maps/api/js/KmlOverlayService.GetFeature",_.Hi)},v9=function(a){this.g=a},w9=function(a,b){this.i=b;this.g=this.j=null;_.H.bind(this.i,"insert",this,this.xp);_.H.bind(this.i,"remove",this,this.yp)},J9a=function(){},x9=function(a,b){return 0==_.oe(a,1)?a.Ab()*b:2==_.oe(a,1)?b-a.Ab():a.Ab()},K9a=function(a,b,c){return 2==_.oe(a,0)?(a=0==_.oe(a.Pb(),1)?a.Pb().Ab()*b:a.Pb().Ab(),a/c):1},L9a=function(a,b,c,d){return 0==_.oe(a,0)?b:2==_.oe(a,0)?
x9(a.Pb(),c):b*d},y9=function(a,b){this.g=b;this.i=_.H.bind(a,"click",this,this.j)},O9a=function(a){var b=a.get("map");0!=a.get("screenOverlays")?M9a(a,b):N9a(a,b)},P9a=function(a){return a.get("url")?a.get("url"):null},S9a=function(a,b,c){b.__gm.ha||(b.__gm.ha={},_.Pe({"false":_.Jr,"true":_.Vr},function(d,e){b.__gm.ha[d]=new m9(new v9(_.ik(_.fr,_.nj,e+"/maps/api/js/KmlOverlayService.GetOverlays",_.Hi)))}));if(a.T=c)a.O=!0,b.__gm.ha[0==c.lastIndexOf("https://",0)].load(c,_.ik(Q9a,_.ik(R9a,a,b,c))),
_.Tg(b,"Lk"),_.Al("Lk","-p",a),a.screenOverlays_changed=_.ik(O9a,a)},R9a=function(a,b,c,d,e,f,g,h,k,l){if(a.get("map")==b&&c==a.T&&a.O){a.O=!1;var m=P9a(a);if(m&&m==c&&(a.set("status",g),"OK"==g)){a.g=h;a.i=k;e&&a.set("defaultViewport",e);a.set("metadata",f);a.$=l;c=0==c.lastIndexOf("https://",0);e=new u9(c?_.Vr:_.Jr);f=_.LA(e);g=new _.Il;g.layerId=d;g.Fm=c;g.zIndex=a.get("zIndex")||0;for(var p in l)g.parameters[p]=l[p];g.Yq=(0,_.Za)(f.load,f);g.clickable=0!=a.get("clickable");a.j=g;_.IBa(g,_.xH(b));
a.H||(a.H=_.H.addListener(g,"click",(0,_.Za)(T9a,a,a,b)));0!=a.get("screenOverlays")&&M9a(a,b);for(d=0;d<a.i.length;++d)l=a.i[d],l.overlay.set("map",b),l.overlay.bindTo("clickable",a),U9a(e,l,a,b);d=a.get("preserveViewport");e=a.get("defaultViewport");!d&&e&&b.fitBounds(e);b=new _.qh;b=new y9(a,b);b.bindTo("map",a);b.bindTo("suppressInfoWindows",a);a.o=b;_.H.addListener(a,"clickable_changed",function(){a.j.clickable=0!=a.get("clickable")})}}},U9a=function(a,b,c,d){var e=new _.jH(c.j.layerId,b.layerId);
c=(0,_.Za)(V9a,c,c,d,b.overlay.get("bounds").getCenter(),null);a=(0,_.Za)(a.load,a,e,c);b.listener=_.H.addListener(b.overlay,"click",a)},V9a=function(a,b,c,d,e){if(!e.infoWindowHtml){b=_.gn("div");b.setAttribute("style","font-family: Roboto,Arial,sans-serif; font-size: small");if(e.info_window_html)_.nu(b,e.info_window_html);else if(e.name||e.description){if(e.name){var f=_.gn("div",b);f.setAttribute("style","font-weight: 500; font-size: medium; margin-bottom: 0em");_.hn(e.name,f)}e.description&&
(f=_.gn("div",b),_.nu(f,e.description))}else b=null;f="";b&&(f=document.createElement("div"),f.appendChild(b),f=f.innerHTML);e.infoWindowHtml=f}_.H.trigger(a,"click",{latLng:c,pixelOffset:d,featureData:e});_.Al("Lk","-i",e)},T9a=function(a,b,c,d,e,f){V9a(a,b,d,e,f)},Q9a=function(a,b){if(b&&a&&0==b.getStatus()){for(var c=[],d=[],e={},f=0;f<_.ze(b,5);++f){var g=new j9(_.xe(b,5,f));if(_.nk(g,5))g={Dh:new i9(g.W[5])},d.push(g);else if(_.nk(g,4)){var h=W9a(new _.sl((new d9(g.W[4])).W[1]));h=new _.rh((new c9((new d9(g.W[4])).W[0])).getUrl(),
h);c.push({overlay:h,layerId:g.getId()})}}g=_.qe(b,1);h=W9a(b.getDefaultViewport());f=new F9a(b.W[3]);var k=new D9a(f.W[3]);k={name:_.qe(f,0),description:_.qe(f,1),snippet:_.qe(f,2),author:{name:_.qe(k,0),email:_.qe(k,2),uri:_.qe(k,1)},hasScreenOverlays:!1};k.hasScreenOverlays=!!d.length;a:{for(l in _.kj)if(_.oe(b,6)==X9a[l]){var l=_.kj[l];break a}l="UNKNOWN"}for(f=0;f<_.ze(b,9);++f){var m=new _.DH(_.xe(b,9,f));e[m.getKey()]=m.Ab()}for(f=0;f<_.ze(b,7);++f)m=new _.DH(_.xe(b,7,f)),e[m.getKey()]=m.Ab();
a(g,h,k,l,d,c,e)}},Y9a=function(a){var b=a.__gm.screenOverlays;return b?b:(b=new _.Bh,a.__gm.screenOverlays=b,(new w9(new J9a,b)).bindTo("innerContainer",a.__gm),b)},N9a=function(a,b){if(a.g){b=Y9a(b);for(var c=0;c<a.g.length;++c)b.remove(a.g[c])}},M9a=function(a,b){if(a.g){b=Y9a(b);for(var c=a.g.length-1;0<=c;--c)_.Ch(b,a.g[c])}},W9a=function(a){var b=new _.rf(_.pe(new _.pl(a.W[1]),0),_.pe(new _.pl(a.W[1]),1));a=new _.rf(_.pe(new _.pl(a.W[0]),0),_.pe(new _.pl(a.W[0]),1));return new _.tg(a,b)},z9=
function(){};_.C(D9a,_.D);var A9;_.C(E9a,_.D);_.C(c9,_.D);c9.prototype.getUrl=function(){return _.qe(this,0)};c9.prototype.setUrl=function(a){this.W[0]=a};_.C(d9,_.D);_.C(e9,_.D);e9.prototype.Ab=function(){return _.pe(this,0)};_.C(f9,_.D);f9.prototype.Pb=function(){return new e9(this.W[1])};f9.prototype.setSize=function(a){this.W[1]=a.W};_.C(g9,_.D);g9.prototype.Sa=function(){return new f9(this.W[0])};g9.prototype.Nd=function(a){this.W[0]=a.W};g9.prototype.Qa=function(){return new f9(this.W[1])};g9.prototype.Od=function(a){this.W[1]=a.W};_.C(h9,_.D);h9.prototype.Sa=function(){return new e9(this.W[0])};h9.prototype.Nd=function(a){this.W[0]=a.W};h9.prototype.Qa=function(){return new e9(this.W[1])};h9.prototype.Od=function(a){this.W[1]=a.W};_.C(i9,_.D);i9.prototype.Pb=function(){return new g9(this.W[3])};i9.prototype.setSize=function(a){this.W[3]=a.W};_.C(j9,_.D);j9.prototype.getId=function(){return _.qe(this,0)};_.C(F9a,_.D);_.C(k9,_.D);k9.prototype.getUrl=function(){return _.qe(this,0)};k9.prototype.setUrl=function(a){this.W[0]=a};var X9a={UNKNOWN:0,OK:1,INVALID_REQUEST:2,DOCUMENT_NOT_FOUND:3,FETCH_ERROR:4,INVALID_DOCUMENT:5,DOCUMENT_TOO_LARGE:6,LIMITS_EXCEEDED:7,INTERNAL_ERROR:8,TIMED_OUT:9,Pz:10};_.C(l9,_.D);l9.prototype.getStatus=function(){return _.oe(this,0,-1)};l9.prototype.getDefaultViewport=function(){return new _.sl(this.W[4])};l9.prototype.Cg=function(a){_.se(this,5).splice(a,1)};l9.prototype.Df=function(){return new j9(_.we(this,5))};m9.prototype.load=function(a,b){this.g++;b=_.Tt((0,_.Za)(this.j,this,b));this.i.load(a,b)};m9.prototype.j=function(a,b){this.Nh.push((0,_.Za)(a,null,b));this.g--;if(0==this.g){for(a=0;a<this.Nh.length;++a)this.Nh[a]();this.Nh=[]}};_.C(o9,_.I);o9.prototype.projection_changed=function(){n9(this)};o9.prototype.bounds_changed=function(){n9(this)};o9.prototype.projectionBounds_changed=function(){_.vi(this.ob)};o9.prototype.mapBounds_changed=function(){_.vi(this.ob)};_.C(r9,_.I);r9.prototype.changed=function(a){"bounds"!=a&&"projection"!=a||_.vi(this.ob)};r9.prototype.j=function(){this.g.forEach(function(a){a.hw&&this.remove(a)})};_.C(t9,_.I);t9.prototype.opacity_changed=function(){var a=s9(this);this.g.forEach(function(b){_.wu(b.node,a)})};t9.prototype.O=function(a){var b=s9(this);this.o(b,a)};t9.prototype.o=function(a,b){var c=b.node=_.QA(this.N,this.j,b.Vw,b.Qq,_.Qj,b.scaledSize);c=b.aq=new _.Br(this.j,10,{image:c,bounds:b.Gz,size:b.Qq},this.i.Ae);this.i.Ob(c);_.wu(b.node,a)};t9.prototype.H=function(a){a.node&&(a.aq&&this.i&&this.i.Bg(a.aq),a.node=null)};u9.prototype.load=function(a,b){var c=new E9a;c.W[0]=a.layerId;c.W[1]=a.g+"";if(a.parameters)for(var d in a.parameters){var e=new _.DH(_.we(c,2));e.W[0]=d;e.W[1]=a.parameters[d]}A9||(A9={oa:"ssM",Ea:["ss"]});a=A9;c=_.pi.g(c.Kb(),a);this.g(c,b,b);return c};u9.prototype.cancel=function(){throw Error("Not implemented");};v9.prototype.load=function(a,b){var c=new k9;c.setUrl(a);a=_.pi.g(c.Kb(),"s3i");c=(0,_.Za)(this.j,this,b);b=(0,_.Za)(this.i,this,b);this.g(a,c,b)};v9.prototype.i=function(a){a(null)};v9.prototype.j=function(a,b){b=new l9(b);a(b)};_.C(w9,_.I);_.n=w9.prototype;_.n.innerContainer_changed=function(){var a=this.g;this.g=this.get("innerContainer");this.j&&(_.H.removeListener(this.j),delete this.j);a&&this.i.forEach((0,_.Za)(this.yp,this));this.g&&(this.j=_.H.bind(this.g,"resize",this,this.oy),this.i.forEach((0,_.Za)(this.xp,this)))};_.n.oy=function(){var a=this;_.Tt(function(){a.i.forEach((0,_.Za)(a.Vp,a))})()};
_.n.xp=function(a){if(this.g){var b=_.$h(this.g);b=_.gn("div",this.g,new _.M(b.width,b.height));_.ln(b);_.mn(b,2);a.nb=b;b=_.gn("div",a.nb,new _.M(0,0),null,!0);_.ln(b);a.Ql=b;b={Lf:(0,_.Za)(this.Et,this,a)};a.image=_.PA((new c9(a.Dh.W[0])).getUrl(),a.nb,null,null,b)}};_.n.yp=function(a){a.nb&&_.Tl(a.nb);a.Ql&&_.Tl(a.Ql);a.image&&_.Tl(a.image);a.nb=null;a.image=null;a.Ql=null};_.n.Et=function(a,b,c){a.nb&&c&&(a.image=c,_.ln(c),this.Vp(a))};
_.n.Vp=function(a){var b=_.$h(this.g);var c=_.$h(a.image);var d=K9a(a.Dh.Pb().Sa(),b.width,c.width),e=K9a(a.Dh.Pb().Qa(),b.height,c.height);e=L9a(a.Dh.Pb().Sa(),c.width,b.width,e);c=L9a(a.Dh.Pb().Qa(),c.height,b.height,d);c=new _.Jg(e,c);d=x9((new h9(a.Dh.W[2])).Sa(),b.width);e=x9((new h9(a.Dh.W[2])).Qa(),b.height);e=b.height-e-c.height;b=x9((new h9(a.Dh.W[1])).Sa(),c.width);var f=x9((new h9(a.Dh.W[1])).Qa(),c.height);_.fn(a.nb,new _.M(d-b,e+f));_.Zh(a.nb,c);_.Zh(a.image,c);_.Zh(a.Ql,c)};_.C(y9,_.I);y9.prototype.remove=function(){this.g.close();_.H.removeListener(this.i);delete this.i};y9.prototype.changed=function(){this.g.close()};y9.prototype.suppressInfoWindows_changed=function(){this.get("suppressInfoWindows")&&this.g.close()};y9.prototype.j=function(a){if(a){var b=this.get("map");if(b&&!this.get("suppressInfoWindows")){var c=a.featureData;if(c=c&&c.infoWindowHtml||a.infoWindowHtml)this.g.setOptions({pixelOffset:a.pixelOffset,position:a.latLng,content:c}),this.g.open(b)}}};z9.prototype.i=function(a){var b=a.V,c=a.V=a.get("map"),d=P9a(a);if(b){a.O=!1;a.j&&_.dCa(a.j,b);a.H&&(_.H.removeListener(a.H),delete a.H);N9a(a,b);delete a.screenOverlays_changed;if(a.i)for(b=0;b<a.i.length;++b){var e=a.i[b];e.overlay.set("map",null);e.listener&&(_.H.removeListener(e.listener),delete e.listener)}a.o&&(a.o.remove(),a.o.unbindAll(),delete a.o);_.Bl("Lk","-p",a)}c&&S9a(a,c,d)};
z9.prototype.g=function(a){var b=a.get("map"),c=b&&b.__gm;a.j&&a.j.$.remove(a);(a.j=c)&&_.Ch(c.$,a);if(c&&!c.ta){var d=H9a(c.$,c);c.ta=d;c.o.register(d)}a.g&&(a.g.set("bounds",null),a.i.unbindAll(),a.g.unbindAll(),a.o.then(function(k){k.unbindAll()}),delete a.i,delete a.g,delete a.o,_.Bl("Og","-p",a));if(b){var e=a.get("bounds"),f=a.get("url"),g=c.get("panes").overlayLayer,h=new _.Bh;a.H=h;d=new o9;d.bindTo("mapBounds",b,"bounds");d.bindTo("projection",b);d.bindTo("zoom",b);d.set("bounds",e);a.i=
d;e=new r9(e,h);e.bindTo("zoom",b);e.bindTo("projection",b);e.bindTo("bounds",d,"croppedBounds");a.g=e;a.o=c.i.then(function(k){k=new t9(f,g,h,k.Qc);k.bindTo("opacity",a);return k});_.Tg(b,"Og");_.Al("Og","-p",a);_.H.addListener(a,"click",function(){_.Al("Og","-i",a)})}};_.Jf("kml",new z9);});
