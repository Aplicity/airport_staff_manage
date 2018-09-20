clc;clear
rand('state',sum(clock));
p0=0;
x0=floor(2*rand(16200,1))
tic
for i=1:10^10
   x=rand(16200,1);
x1=floor(x);x2=ceil(x);
[f,g]=test(x1);
if sum(g<=0)==1200
   if p0<=f
      x0=x1;p0=f;
   end
end
[f,g]=test(x2);
if sum(g<=0)==1200
   if p0<=f
      x0=x2;p0=f;
   end
end
end
x0,
p0 
toc
