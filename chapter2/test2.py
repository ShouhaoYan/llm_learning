from langchain_community.document_loaders import WebBaseLoader
from langchain_community.llms import Tongyi
from utils.ds_util import sample_call_streaming
from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader(r"D:\Users\sinoflow_eng4\Desktop\ANSYS20222-芯片散热的机器学习.docx")

data = loader.load()

data

llm = Tongyi()
llm.model_name = 'qwen-max'


def load_doc_content(url):
    loader = WebBaseLoader(url)
    doc = loader.load()
    return doc[0].page_content

doc_content_cn = data
# doc_content_cn = load_doc_content("https://a.afbza.cn/preview/file?pageCount=7&file_type=pdf&id=1094074&url=https%3A%2F%2Fbmwfileres.bmwax.cn%2Fmqrcode%2Fmqrfile%2F575276%2F1722916701_5757312700_%E7%94%B5%E5%8A%A8%E6%B1%BD%E8%BD%A6%E7%94%B5%E6%B1%A0%E7%83%AD%E7%AE%A1%E7%90%86.pdf&preview_url=convert%2Fmqrcode%2Fmqrfile%2F575276%2F1722916701_5757312700_%E7%94%B5%E5%8A%A8%E6%B1%BD%E8%BD%A6%E7%94%B5%E6%B1%A0%E7%83%AD%E7%AE%A1%E7%90%86&short=PL7GWF&domain=w.afbcs.cn&sign=&d=true&t=%E7%94%B5%E5%8A%A8%E6%B1%BD%E8%BD%A6%E7%94%B5%E6%B1%A0%E7%83%AD%E7%AE%A1%E7%90%86&tips=")
doc_content_intl = load_doc_content("https://www.alibabacloud.com/help/zh/ecs/user-guide/create-a-subscription-instance-on-the-quick-launch-tab")

prompt = f"""你现在的任务是总结下面这篇文档主要内容。
--------
【中国站的文档】：
{doc_content_cn}
--------
【国际站的文档】:
{doc_content_intl}
--------
请给出结论，并用列表形式指出不同之处的具体位置：
"""

sample_call_streaming(prompt)