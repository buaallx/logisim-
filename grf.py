with open('grfdata.txt', 'w') as f:
    for i in range(0, 16):
        print(f'''<wire from="(400,{260+60*i})" to="(410,{260+60*i})"/>
    <wire from="(400,{230+60*i})" to="(410,{230+60*i})"/>
    <wire from="(440,{260+60*i})" to="(450,{260+60*i})"/>
    <wire from="(140,{260+60*i})" to="(150,{260+60*i})"/>
    <wire from="(180,{260+60*i})" to="(190,{260+60*i})"/>
    <wire from="(140,{230+60*i})" to="(150,{230+60*i})"/>
    <wire from="(180,{240+60*i})" to="(220,{240+60*i})"/>
    <wire from="(80,{240+60*i})" to="(150,{240+60*i})"/>
    <wire from="(440,{240+60*i})" to="(480,{240+60*i})"/>
    <wire from="(340,{240+60*i})" to="(410,{240+60*i})"/>
    <comp lib="0" loc="(400,{260+60*i})" name="Tunnel">
        <a name="facing" val="east"/>
        <a name="label" val="clk"/>
    </comp>
    <comp loc="(440,{240+60*i})" name="memory"/>
    <comp lib="0" loc="(340,{240+60*i})" name="Tunnel">
        <a name="facing" val="east"/>
        <a name="label" val="in_check{16+i}"/>
    </comp>
    <comp loc="(180,{240+60*i})" name="memory"/>
    <comp lib="0" loc="(450,{260+60*i})" name="Tunnel">
        <a name="label" val="reset"/>
    </comp>
    <comp lib="0" loc="(480,{240+60*i})" name="Tunnel">
        <a name="width" val="32"/>
        <a name="label" val="out{16+i}"/>
    </comp>
    <comp lib="0" loc="(140,{230+60*i})" name="Tunnel">
        <a name="facing" val="east"/>
        <a name="width" val="32"/>
        <a name="label" val="WD"/>
    </comp>
    <comp lib="0" loc="(400,{230+60*i})" name="Tunnel">
        <a name="facing" val="east"/>
        <a name="width" val="32"/>
        <a name="label" val="WD"/>
    </comp>
    <comp lib="0" loc="(220,{240+60*i})" name="Tunnel">
        <a name="width" val="32"/>
        <a name="label" val="out{i}"/>
    </comp>
    <comp lib="0" loc="(140,{260+60*i})" name="Tunnel">
        <a name="facing" val="east"/>
        <a name="label" val="clk"/>
    </comp>
    <comp lib="0" loc="(80,{240+60*i})" name="Tunnel">
        <a name="facing" val="east"/>
        <a name="label" val="in_check{i}"/>
    </comp>
    <comp lib="0" loc="(190,{260+60*i})" name="Tunnel">
        <a name="label" val="reset"/>
    </comp>''', file=f)
        