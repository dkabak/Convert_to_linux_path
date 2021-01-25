import os, sys, re, glob


#find_replace_list= [{"[d|D][:]","/bigdisk0/apps"},{"[\\\\]","/"},{"(\.exe)", ".bin"}]
# pattern1 = re.compile("[d|D][:]",re.MULTILINE)
# pattern2 = re.compile("[\\\\]")
# pattern3 = re.compile("(\.exe)")
# pattern4 = re.compile("[@][d|D][:]",re.MULTILINE)
# replacementStringMatchesPattern1 = "/bigdisk0/apps"
# replacementStringMatchesPattern2 = "/"
# replacementStringMatchesPattern3 = ".bin"


files=glob.glob('d:/tmp/kabakdmy/converted ini/**/*.ini', recursive=True)

for infile in files:
   #print (infile)
   new_content=""
   reader = open(infile, "r")
   file_content=reader.readlines()
   reader.close()
   output_file = open(infile, 'w')
   output_file.seek(0)
   for line in file_content:
      retline1 = re.sub(r"([d|D]:\\\\)", "/bigdisk0/apps/", line, flags=re.MULTILINE)
      retline2 = re.sub(r"(\\\\)", "/", retline1, flags=re.MULTILINE)
      retline3 = re.sub(r"([d|D]:\\)","/bigdisk0/apps/", retline2, flags=re.MULTILINE)
      retline4 = re.sub("(\.exe)", ".bin", retline3, flags=re.MULTILINE)
      retline5 = re.sub(r"(\\)", "/", retline4, flags=re.MULTILINE)
      retline6 = re.sub(r"(smemmux])","unixsmemmux]",retline5,flags=re.MULTILINE)
      retline7 = re.sub(r"(smem])", "unixsmem]", retline6, flags=re.MULTILINE)
      retline8 = re.sub(r"(smemmux$)", "unixsmemmux", retline7, flags=re.MULTILINE)
      retline9 = re.sub(r"(smem$)", "unixsmem", retline8, flags=re.MULTILINE)

      new_content=retline9
      output_file.write(new_content)
   output_file.close()
