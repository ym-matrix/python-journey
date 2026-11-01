medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three =sorted(medals.keys(),key=lambda medal:medals[medal],reverse=True )
print(top_three)