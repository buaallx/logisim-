with open("grfdata2.txt", "w") as f:
    for i in range(32):
        t = i % 4
        t *= 70
        print(f'''    <wire from="(240,{1990+10*i})" to="({250+t},{1990+10*i})"/>
    <comp lib="0" loc="({250+t},{1990+10*i})" name="Tunnel">
      <a name="width" val="1"/>
      <a name="label" val="in_check{i}"/>
    </comp>''', file=f)