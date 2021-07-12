clear all
close all
clc

%% Set up the Import Options and import the data
opts = spreadsheetImportOptions("NumVariables", 32);

% Specify sheet and range
opts.Sheet = "Day 1";
opts.DataRange = "A1:AF911";

% Specify column names and types
opts.VariableNames = ["VarName1", "VarName2", "VarName3", "VarName4", "VarName5", "VarName6", "VarName7", "VarName8", "VarName9", "VarName10", "VarName11", "VarName12", "VarName13", "VarName14", "VarName15", "VarName16", "VarName17", "VarName18", "VarName19", "VarName20", "VarName21", "VarName22", "VarName23", "VarName24", "VarName25", "VarName26", "VarName27", "VarName28", "VarName29", "VarName30", "VarName31", "VarName32"];
opts.VariableTypes = ["char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char", "char"];

% Specify variable properties
opts = setvaropts(opts, ["VarName1", "VarName2", "VarName3", "VarName4", "VarName5", "VarName6", "VarName7", "VarName8", "VarName9", "VarName10", "VarName11", "VarName12", "VarName13", "VarName14", "VarName15", "VarName16", "VarName17", "VarName18", "VarName19", "VarName20", "VarName21", "VarName22", "VarName23", "VarName24", "VarName25", "VarName26", "VarName27", "VarName28", "VarName29", "VarName30", "VarName31", "VarName32"], "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["VarName1", "VarName2", "VarName3", "VarName4", "VarName5", "VarName6", "VarName7", "VarName8", "VarName9", "VarName10", "VarName11", "VarName12", "VarName13", "VarName14", "VarName15", "VarName16", "VarName17", "VarName18", "VarName19", "VarName20", "VarName21", "VarName22", "VarName23", "VarName24", "VarName25", "VarName26", "VarName27", "VarName28", "VarName29", "VarName30", "VarName31", "VarName32"], "EmptyFieldRule", "auto");

% Import the data
Day1 = readtable("C:\Users\kwira\Downloads\Day_1.xlsx", opts, "UseExcel", false);

% Convert to output type
Day1 = table2cell(Day1);
numIdx = cellfun(@(x) ~isnan(str2double(x)), Day1);
Day1(numIdx) = cellfun(@(x) {str2double(x)}, Day1(numIdx));

% Clear temporary variables
clear opts

%%
sz = size(Day1);
szz = sz(1,2);
szzz = sz + 1;
x = Day1(:,1);
xx = cell2mat(x);
n = 2;

while n ~= szzz
    y = Day1(:,n);
    yy = cell2mat(y);
    trial = n - 1;
    zz = trial.* ones(length(x),1);
    scatter3(zz,xx,yy,15,'.')
    hold on
    
    n = n + 1;
end

title('Quartz Sample 5 Day 1 Irradiations','fontsize',16)
ylabel('Wavelength [nm]','fontsize',16)
zlabel('Percent Tranmission','fontsize',16)
xlabel('Scan Number','fontsize',16);
ax = gca;
ax.YDir = 'reverse';

%% Manual adjustment
xlim([0,32]);
xticks(0:(35/7):35);
ylim([0,1200]);
yticks(0:(1200/6):1100);

zlim([0,101]);
zticks(0:(100/5):100);


%%
zpoint = linspace(0,100);
zzpoint = reshape(zpoint,[1,100]);

x1 = linspace(1,31,100);
y1 = 200.* ones(length(x1),1);
z1 = 0.* ones(length(x1),1);
plot3(x1, y1, z1,'color','b','linewidth',3)

x1 = linspace(1,31,100);
y1 = 600.* ones(length(x1),1);
z1 = 0.* ones(length(x1),1);
plot3(x1, y1, z1,'color','b','linewidth',3)

y1 = linspace(200,600,100);
x1 = 1.* ones(length(y1),1);
z1 = 0.* ones(length(y1),1);
plot3(x1, y1, z1,'color','b','linewidth',3)

y1 = linspace(200,600,100);
x1 = 31.* ones(length(y1),1);
z1 = 0.* ones(length(y1),1);
plot3(x1, y1, z1,'color','b','linewidth',3)


x2 = linspace(1,31,100);
y2 = 200.* ones(length(x2),1);
z2 = 100.* ones(length(x2),1);
plot3(x2, y2, z2,'color','b','linewidth',3)

x2 = linspace(1,31,100);
y2 = 600.* ones(length(x2),1);
z2 = 100.* ones(length(x2),1);
plot3(x2, y2, z2,'color','b','linewidth',3)

y2 = linspace(200,600,100);
x2 = 1.* ones(length(y2),1);
z2 = 100.* ones(length(y2),1);
plot3(x2, y2, z2,'color','b','linewidth',3)

y2 = linspace(200,600,100);
x2 = 31.* ones(length(y2),1);
z2 = 100.* ones(length(y2),1);
plot3(x2, y2, z2,'color','b','linewidth',3)


z3 = linspace(0,100,100);
y3 = 200.* ones(length(z3),1);
x3 = 1.* ones(length(z3),1);
plot3(x3, y3, z3,'color','b','linewidth',3)

z3 = linspace(0,100,100);
y3 = 200.* ones(length(z3),1);
x3 = 31.* ones(length(z3),1);
plot3(x3, y3, z3,'color','b','linewidth',3)

z3 = linspace(0,100,100);
y3 = 600.* ones(length(z3),1);
x3 = 1.* ones(length(z3),1);
plot3(x3, y3, z3,'color','b','linewidth',3)

z3 = linspace(0,100,100);
y3 = 600.* ones(length(z3),1);
x3 = 31.* ones(length(z3),1);
plot3(x3, y3, z3,'color','b','linewidth',3)