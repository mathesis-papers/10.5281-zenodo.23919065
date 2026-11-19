'use strict';
// All diagrams are schematic. A block marked H represents all 33 vertices.
function heading(en, zh) {
  txt(en, W/2, 218, {size:48,fam:F.disp,w:700,align:'center',c:C.white});
  txt(zh, W/2, 275, {size:30,fam:F.zh,align:'center',c:C.dim});
}
function edge(x1,y1,x2,y2,a=1,c=C.cyan) {
  ctx.save();ctx.globalAlpha=a;ctx.strokeStyle=c;ctx.lineWidth=5;
  ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();ctx.restore();
}
function node(x,y,label,chosen=false,a=1) {
  ctx.save();ctx.globalAlpha=a;ctx.fillStyle=chosen?C.now:C.cyan;
  ctx.beginPath();ctx.arc(x,y,chosen?19:13,0,Math.PI*2);ctx.fill();ctx.restore();
  if(label)txt(label,x,y+55,{size:28,fam:F.math,align:'center',c:chosen?C.now:C.white,a});
}
function pair(x,y,sel,a=1) {
  edge(x-65,y,x+65,y,a);node(x-65,y,'a',sel.includes('a'),a);node(x+65,y,'b',sel.includes('b'),a);
}
function piece(x,y,label,selected='w',a=1) {
  panel(x-205,y-140,410,300,a,C.cyan);
  txt(label,x,y-80,{size:33,fam:F.disp,align:'center',c:C.white,a});
  edge(x,y,x,y+80,a);node(x,y,'',selected==='v',a);node(x,y+80,'',selected==='w',a);
  txt('v',x+35,y-22,{size:28,fam:F.math,c:C.white,a});txt('w',x+35,y+88,{size:28,fam:F.math,c:C.white,a});
  txt('rest of piece / 其余顶点',x,y+132,{size:19,fam:F.zh,align:'center',c:C.dim,a});
}
function hBlock(x,y,label,a=1) {
  panel(x-180,y-125,360,250,a,C.cyan);
  txt(label,x,y-45,{size:42,fam:F.disp,align:'center',c:C.white,a});
  edge(x,y+20,x,y+78,a);node(x,y+20,'',false,a);node(x,y+78,'',false,a);
  txt('4',x+30,y-8,{size:24,fam:F.math,c:C.white,a});
  txt('5 (leaf)',x+30,y+90,{size:20,fam:F.math,c:C.dim,a});
}
SCENES.choices = S => {
  badgeQ(S,[[0,null,'computed']]);heading('Three covering choices','一条边，三个支配集');
  const labels=['{a}','{b}','{a,b}'], sels=['a','b','ab'];
  for(let j=0;j<3;j++) {
    const x=420+j*540, a=at(S,1,0.8,j*0.4);
    panel(x-220,340,440,340,a,C.cyan);pair(x,465,sels[j],a);
    txt(labels[j],x,610,{size:34,fam:F.math,align:'center',c:C.white,a});
  }
  txt('D(K₂,x) = 2x + x²       D(K₂,−4) = 8',W/2,790,{size:41,fam:F.math,align:'center',c:C.white,a:at(S,2,0.6)});
};
SCENES.obstacle = S => {
  badgeQ(S,[[0,null,'argued'],[2,null,'computed']]);heading('Connecting can change the count','连通，不一定保留计数');
  const a=at(S,1,0.7), t=Q(S,2,'Add an edge');
  panel(250,350,600,350,1,C.cyan);txt('two isolated vertices',550,415,{size:28,align:'center',c:C.white});
  node(440,520,'a',true);node(660,520,'b',true);
  txt('x²',550,650,{size:45,fam:F.math,align:'center',c:C.white});
  panel(1070,350,600,350,a,C.cyan);txt('new singleton choices',1370,415,{size:28,align:'center',c:C.white,a});
  edge(1260,520,1480,520,t);node(1260,520,'a',true,a);node(1480,520,'b',false,a);
  txt('x² + 2x',1370,650,{size:45,fam:F.math,align:'center',c:C.white,a:t});
  txt('A special attachment point is needed',W/2,790,{size:34,fam:F.disp,align:'center',c:C.white,a:t});
};
SCENES.leaf = S => {
  badgeQ(S,[[0,null,'argued']]);heading('The leaf protects the support','叶子迫使支撑点在内部被覆盖');
  const swap=at(S,0,0.8,6), link=Q(S,1,'join only supports');
  piece(500,510,'piece i',swap>0.6?'v':'w');piece(1420,510,'piece j','w');
  edge(500,510,1420,510,link,C.argued);
  txt('new edges touch supports only',W/2,735,{size:31,fam:F.disp,align:'center',c:C.argued,a:link});
  txt('restrict  ↔  unite     |S| = Σ |Sᵢ|',W/2,805,{size:35,fam:F.math,align:'center',c:C.white,a:at(S,2,0.6)});
};
SCENES.chain = S => {
  badgeQ(S,[[0,null,'argued']]);heading('One copy, one factor','每多一份，就多一个因子');
  const a=at(S,0,0.8), link=at(S,1,0.8);
  for(let j=0;j<3;j++) hBlock(450+j*510,495,'H'+(j+1),a);
  edge(450,515,960,515,link,C.argued);edge(960,515,1470,515,link,C.argued);
  txt('D(Gᵣ,x) = D(H,x)ʳ',W/2,725,{size:48,fam:F.math,align:'center',c:C.white,a:link});
  txt('33r vertices    multiplicity r    maximum degree 7',W/2,805,{size:31,fam:F.disp,align:'center',c:C.white,a:at(S,2,0.7)});
};
SCENES.sizes = S => {
  badgeQ(S,[[0,null,'argued']]);heading('Fill the gaps with 2 and 3','两点、三点填满每个至少 35 的阶');
  panel(180,350,700,350,1,C.cyan);txt('35 = 33 + 2',530,420,{size:44,fam:F.math,align:'center',c:C.white});
  hBlock(410,535,'H',0.7);pair(740,555,'',1);edge(410,555,675,555,at(S,0,0.8),C.argued);
  panel(1040,350,700,350,1,C.cyan);txt('36 = 33 + 3',1390,420,{size:44,fam:F.math,align:'center',c:C.white});
  hBlock(1245,535,'H',0.7);edge(1580,495,1580,605);node(1580,495,'');node(1580,550,'');txt('v',1615,558,{size:24,fam:F.math,c:C.white});node(1580,605,'');edge(1245,555,1580,550,at(S,0,0.8),C.argued);
  txt('D(K₂,−4) = 8     D(P₃,−4) = −20',W/2,760,{size:36,fam:F.math,align:'center',c:C.white,a:at(S,1,0.7)});
  txt('n ≥ 35   ·   simple root   ·   cycle rank 4',W/2,825,{size:33,fam:F.math,align:'center',c:C.white,a:at(S,2,0.7)});
};
SCENES.scope = S => {
  badgeQ(S,[[0,null,'lean'],[1,null,'argued']]);heading('Connected examples beyond every threshold','任意大小上界之外，都有连通例子');
  panel(270,345,1380,245,1,C.cyan);
  txt('For every N, some connected G has',W/2,425,{size:38,fam:F.disp,align:'center',c:C.white});
  txt('|V(G)| > N       D(G,−4) = 0',W/2,520,{size:50,fam:F.math,align:'center',c:C.white});
  txt('Path degrees, multiplicities, every order: written proofs',W/2,675,{size:30,fam:F.disp,align:'center',c:C.argued,a:at(S,1,0.7)});
  txt('Haobo Ma · Wenlin Zhang',W/2,755,{size:30,fam:F.disp,align:'center',c:C.white,a:at(S,2,0.7)});
  txt('Based on Alikhani–Griswold and earlier irrelevant-edge theory',W/2,810,{size:24,fam:F.disp,align:'center',c:C.dim,a:at(S,2,0.7)});
};
FILM.poster = () => {
  heading('A leaf preserves a root','一片叶子保住一个根');
  for(let j=0;j<3;j++) hBlock(450+j*510,495,'H'+(j+1));
  edge(450,515,960,515,1,C.argued);edge(960,515,1470,515,1,C.argued);
  txt('D(Gᵣ,x) = D(H,x)ʳ',W/2,735,{size:54,fam:F.math,align:'center',c:C.white});
  txt('Connect the supports. Preserve every choice.',W/2,815,{size:32,fam:F.disp,align:'center',c:C.white});
  txt('Haobo Ma · Wenlin Zhang',W/2,910,{size:26,fam:F.disp,align:'center',c:C.dim});
};
