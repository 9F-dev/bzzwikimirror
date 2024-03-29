FROM ubuntu

RUN cd ~ \
    && apt-get update \
    && apt-get install wget sed python3 python3-pip -y \
    && pip3 install requests \
    && wget https://download.openzim.org/release/zim-tools/zim-tools_linux-x86_64-3.1.0.tar.gz \
    && tar xzvf zim-tools_linux-x86_64-3.1.0.tar.gz \
    && rm zim-tools_linux-x86_64-3.1.0.tar.gz

COPY mirror.py mirror.py

COPY entry.sh entry.sh 

ENTRYPOINT ["sh","entry.sh"]

CMD ["https://download.kiwix.org/zim/wikipedia/wikipedia_bm_all_maxi_2022-02.zim"]
