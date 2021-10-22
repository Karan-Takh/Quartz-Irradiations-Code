#Use TransDosage1
#These wavelengths were picked because of the different trends of percent transmittance

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker

df = pd.read_csv('TransDosage1.csv')

transmittances = df.iloc[81].tolist()
transmittances = transmittances[3:]
print(transmittances)

transmittance = df.iloc[171].tolist()
transmittance = transmittance[3:]
print(transmittance)

transmittanc = df.iloc[246].tolist()
transmittanc = transmittanc[3:]
print(transmittanc)

transmittan = df.iloc[393].tolist()
transmittan = transmittan[3:]
print(transmittan)

columns = df.iloc[0].tolist()
columns = columns[3:]
print(columns)

class MathTextSciFormatter(mticker.Formatter):
    def __init__(self, fmt="%1.2e"):
        self.fmt = fmt
    def __call__(self, x, pos=None):
        s = self.fmt % x
        decimal_point = '.'
        positive_sign = '+'
        tup = s.split('e')
        significand = tup[0].rstrip(decimal_point)
        sign = tup[1][0].replace(positive_sign, '')
        exponent = tup[1][1:].lstrip('0')
        if exponent:
            exponent = '10^{%s%s}' % (sign, exponent)
        if significand and exponent:
            s =  r'%s{\times}%s' % (significand, exponent)
        else:
            s =  r'%s%s' % (significand, exponent)
        return "${}$".format(s)


plt.plot(columns, transmittances, 'o', color='r', label = '270' )
plt.plot(columns, transmittance, 'o', color='m', label = '360' )
plt.plot(columns, transmittanc, 'o', color='b', label = '435' )
plt.plot(columns, transmittan, 'o', color='k', label = '582' )
plt.legend(title = 'Wavelength (nm):', loc ='upper left')
plt.xlabel('Dosage (pulses as arbitrary units)')
plt.ylabel('%T')
plt.ylim(0,51)
plt.gca().xaxis.set_major_formatter(MathTextSciFormatter("%1.2e"))
#plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.title("Percent Transmittance as a function of Dosage", loc="center", fontsize = "20")

sub_axes = plt.axes([.745, .625, .15, .25])
sub_axes.plot(columns, transmittances,'o', color='r')
sub_axes.plot(columns, transmittance,'o', color='m')
sub_axes.plot(columns, transmittanc,'o', color='b')
sub_axes.plot(columns, transmittan,'o', color='k')
sub_axes.set_xlim([0,50000])
plt.show()


