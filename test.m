function [f,g]=cal(x);

%% 目标函数
f1 = 0 ; f2 = 0 ; f3 = 0
for i =1:5400
    f1 = 7*x(i)+f1
end

for i = 5401:10800
    f2 = 8*x(i)+f2
end


for i = 10801:16200
    f3 = 9*x(i)+f2
end

f = -(f1+f2+f3)

%% 第一条限制
g0 = 0

for i = 1:60
    for j = (i-1)*180+1:(i-1)*180+60
        g0 = x(j)+g0
    end
    
    g1(i) = 8-g0
end

g1 = g1'

g0 = 0

for i = 61:90
    for j = (i-1)*180+1:(i-1)*180+60
        g0 = x(j)+g0
    end
    
    g2(i) = 4-g0
end
g2 = g2'
%% 第二条限制

g0 = 0

for i = 1:60
    for j = (i-1)*180+61:180*i
        g0 = x(j)+g0
    end
    
    g3(i) = 12-g0
end

g3 = g3'

g0 = 0

for i = 61:90
    for j = (i-1)*180+61:180*i
        g0 = x(j)+g0
    end
    
    g4(i) = 6-g0
end

g4 = g4'

%% 第三条限制
g0 = 0
for i = 1:180
    for j = 1:28
        g5(i) = 2-(x(180*j-180+i)+x(180*j+i)+x(180*j+180+i))
    end
end

for i = 1:180
    for j = 31:58
        g6(i) = 2-(x(180*j-180+i)+x(180*j+i)+x(180*j+180+i))
    end
end

for i = 1:180
    for j = 61:88
        g7(i) = 2-(x(180*j-180+i)+x(180*j+i)+x(180*j+180+i))
    end
end
g5 = g5'
g6 = g6'
g7 = g7'

%% 第四条限制
for i = 1:180
    for j = 31:59
        g8(i) = 1-(x(180*j-180+i)+x(180*j+i))
    end
end
g8 = g8'

%% 第五条限制
for i =1:180
    for j = 1:84
        g9 = x(180*j-180+i)+x(180*j+i)+x(180*(j+1)+i)+x(180*(j+2)+i)+x(180*(j+3)+i)+x(180*(j+4)+i)+x(180*(j+5)+i)
     g9(i) = 40 - g9*8
    end
end

g9 = g9'

g=[g1
    g2
    g3
    g4
    g5
    g6
    g7
    g8
    g9]


    