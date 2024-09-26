with open("autodata.txt", 'w') as f:
    for i in range(1, 11):
        print(f'''    <wire from="(140,{80+50*i})" to="(150,{80+50*i})"/>
    <wire from="(180,{80+50*i})" to="(190,{80+50*i})"/>
    <comp lib="0" loc="(140,{80+50*i})" name="Tunnel">
        <a name="facing" val="east"/>
        <a name="width" val="8"/>
        <a name="label" val="in{i}"/>
    </comp>
    <comp lib="0" loc="(190,{80+50*i})" name="Tunnel">
        <a name="width" val="8"/>
        <a name="label" val="out{i}"/>
    </comp>
    <comp lib="4" loc="(180,{80+50*i})" name="Register"/>''', file=f)
          
          
        