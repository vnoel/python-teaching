
low_mean = ma.mean(cblow)
# ou
low_mean = cblow.mean()

# quelques suggestions pour agrementer le plot

plot(dates, cblow, color='red', label='Low clouds, mean = %5.2f' % (low_mean))

legend()

xlabel('Time')

ylabel('Altitude [m]')

grid()

# a essayer : subplot