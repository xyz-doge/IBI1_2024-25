import re
TATApattern = 'TATA[AT]A[AT]'
f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
out = open('tata_genes.fa', 'w')
genename = ""
sequence = ""
# 一行一行读取
for line in f:
    line = line.strip()  # 去掉每行末尾的换行符

    # 如果是基因名（以 > 开头）
    if line.startswith('>'):
        # 如果已经有前一条基因的序列了，先检查它
        if sequence != '':
            hastata = re.search(TATApattern, sequence)
            if hastata:
                out.write(genename + '\n')
                out.write(sequence + '\n')

        # 保存新的基因名，只保留第一个单词
        parts = line.split()
        genename = '>' + parts[0][1:]  # 去掉开头的 >
        sequence = ''  # 新基因开始，序列清空

    else:
        # 是序列，把它加到当前的 sequence 中
        sequence = sequence + line

# 文件最后一条基因可能没被处理，我们手动再检查一次
if sequence != '':
    has_tata = re.search(TATApattern, sequence)
    if has_tata:
        out.write(genename + '\n')
        out.write(sequence + '\n')

# 关闭文件
f.close()
out.close()
