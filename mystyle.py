import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

class MyGraphStyle:
    def __init__(self, style, color_name):
        # 기본 스타일 설정
        self.style = {
            'mono': {
                # figure 스타일
                'figure.figsize':(10,6),
                'figure.facecolor':'#000000', # 그래프 배경색 : 블랙
                'figure.edgecolor':'#F9F871', # 그래프 테두리 색 : 그레이
                # Axes
                'axes.titlepad':50,
                'axes.facecolor':'#000000', # 축 배경색 : 블랙
                'axes.edgecolor':'#2A272A', # 축 테두리 색 : 그레이
                'axes.grid':True, # 그리드 표시 여부
                'axes.titlesize':50, # 축 제목의 크기
                'axes.titleweight':'bold', # 제목 두께 설정 'normal', 'bold', 'heavy', 'light', 'ultrabold', 'ultralight'
                'axes.titlecolor':'#FFFFFF',
                'axes.labelsize':15, # 축 레이블의 크기
                'axes.labelpad': 15,  # 레이블 패딩
                'axes.labelcolor':'#FFFFFF', # 축 레이블 색상
                'axes.spines.top':True, # 위쪽 테두리 설정할 것인지
                'axes.spines.bottom':True, # 아래쪽 테두리 설정할 것인지
                'axes.spines.left':True, # 왼쪽 테두리 설정할 것인지
                'axes.spines.right':True, # 오른쪽 테두리 설정할 것인지
                # Grid
                'grid.color':'#2A272A', # 그리드 컬러
                'grid.linestyle':'-', # 그리드 선 스타일 "-", ":", "--"
                'grid.linewidth':1, # 그리드 선 두께
                # Tick 스타일
                'xtick.color':'#677381', #x축 눈금 색상
                'ytick.color':'#677381', # y축 눈금 색상
                'xtick.direction':'in', # x축 눈금 방향 'in', 'out', 'inout'
                'ytick.direction':'in', # y축 눈금 방향
                'xtick.major.size':3, # x축 주요 눈금의 크기
                'xtick.minor.size':3, # x축 주요 눈금의 크기
                'ytick.major.size':3, # y축 주요 눈금의 크기
                'ytick.minor.size':3, # y축 주요 눈금의 크기
                # Font
                'font.size':12, # 전체 폰트 크기
                #'font.family': , # 폰트 패밀리
                'font.style':'normal', #폰트 스타일 'normal', 'italic'
                'font.weight':'normal', # 폰트 두께 'normal', 'bold'
                'text.color':'#FFFFFF',
                # Line
                'lines.linewidth':10, # 선의 굵기

            },
            'clean': {
                # figure 스타일
                'figure.figsize':(10,6),
                'figure.facecolor':'#FFFFFF', # 그래프 배경색 : 화이트
                'figure.edgecolor':'#474554', # 그래프 테두리 색 : 그레이
                # Axes
                'axes.titlepad':50,
                'axes.facecolor':'#FFFFFF', # 축 배경색 : 화이트
                'axes.edgecolor':'#272525', # 축 테두리 색 : 그레이
                'axes.grid':False, # 그리드 표시 여부
                'axes.titlesize':50, # 축 제목의 크기
                'axes.titleweight':'bold', # 제목 두께 설정 'normal', 'bold', 'heavy', 'light', 'ultrabold', 'ultralight'
                'axes.titlecolor':'#000000',
                'axes.labelsize':15, # 축 레이블의 크기
                'axes.labelpad': 15,  # 레이블 패딩
                'axes.labelcolor':'#272525', # 축 레이블 색상
                'axes.spines.top':False, # 위쪽 테두리 설정할 것인지
                'axes.spines.bottom':True, # 아래쪽 테두리 설정할 것인지
                'axes.spines.left':True, # 왼쪽 테두리 설정할 것인지
                'axes.spines.right':False, # 오른쪽 테두리 설정할 것인지
                # Grid
                'grid.color':'#F2E9E9', # 그리드 컬러
                'grid.linestyle':'-', # 그리드 선 스타일 "-", ":", "--"
                'grid.linewidth':1, # 그리드 선 두께
                # Tick 스타일
                'xtick.color':'#272525', #x축 눈금 색상
                'ytick.color':'#272525', # y축 눈금 색상
                'xtick.direction':'in', # x축 눈금 방향 'in', 'out', 'inout'
                'ytick.direction':'in', # y축 눈금 방향
                'xtick.major.size':3, # x축 주요 눈금의 크기
                'xtick.minor.size':3, # x축 주요 눈금의 크기
                'ytick.major.size':3, # y축 주요 눈금의 크기
                'ytick.minor.size':3, # y축 주요 눈금의 크기
                # Font
                'font.size':12, # 전체 폰트 크기
                #'font.family': , # 폰트 패밀리
                'font.style':'normal', #폰트 스타일 'normal', 'italic'
                'font.weight':'normal', # 폰트 두께 'normal', 'bold'
                'text.color':'#000000',
                # Line
                'lines.linewidth':10, # 선의 굵기

            }

        }.get(style, {})

        plt.rcParams.update(self.style)

        # 컬러맵 설정
        colors = {
            'bright': ['#845EC2', '#D65DB1', '#FF6F91', '#FF9671', '#FFC75F', '#F9F871'],
            'cool': ['#845EC2', '#2C73D2', '#0081CF', '#0089BA', '#008E9B', '#008F7A'],
            'calm': ['#845EC2', '#4B4453', '#B0A8B9', '#C34A36', '#FF8066'],
            'summer': ['#845EC2', '#009EFA', '#00D2FC', '#4FFBDF'],
            'dust': ['#845EC2', '#4B4453', '#B0A8B9', '#FF8066'],
            'nature': ['#D03B29', '#A76500', '#6D7E00', '#008B34', '#009278', '#0092B4'],
            'sky': ['#D03B29', '#D99585', '#FFE5DA', '#54B9C9'],
            'default': ['#2F4858', '#98B2C5', '#445D6E', '#0E2938', '#132D3C']
        }.get(color_name, ['#2F4858', '#98B2C5', '#445D6E', '#0E2938', '#132D3C'])

        # 컬러 코드를 RGB로 변환
        rgb_colors = [mcolors.to_rgba(c) for c in colors]
        # 컬러맵 만들기
        self.custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_cmap', rgb_colors, N=256)

    def plot(self, x, y, plot_type='scatter', color=None, **kwargs):
        if plot_type == 'line':
            plt.plot(x, y, color=self.custom_cmap(np.random.rand()), **kwargs)  # 여기에서 커스텀 컬러맵 적용
        elif plot_type == 'scatter':
            plt.scatter(x, y, color=self.custom_cmap(np.random.rand()), **kwargs)
        elif plot_type == 'bar':
            plt.bar(x, y, color=self.custom_cmap(np.random.rand()), **kwargs)
        elif plot_type == 'box':
            colors = [self.custom_cmap(np.random.rand()) for _ in range(len(y))]
            box = plt.boxplot(y, patch_artist=True, **kwargs)
            for patch, color in zip(box['boxes'], colors):
                patch.set_facecolor(color)
            if x is not None and isinstance(x, list):
                plt.xticks(range(1, len(x) + 1), x)
        else:
            raise ValueError('Unsupported plot type')
