with open("grfdata1.txt", 'w') as f:
    for i in range(0, 32):
        t = i % 4
        t *= 40
        print(f'''    <wire from="({170-t},{1200+10*i})" to="(180,{1200+10*i})"/>
    <comp lib="0" loc="({170-t},{1200+10*i})" name="Tunnel">
      <a name="facing" val="east"/>
      <a name="width" val="32"/>
      <a name="label" val="out{i}"/>
    </comp>''', file=f)