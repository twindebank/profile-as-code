"""
cv = CVRenderer(
    censor=False,
    include_sections=[]
)

cv = CVRenderer(
    censor=True,
    include_sections=[]
)



"""
from path import Path

from pyprofile.renderers.texcv.renderer import CVRenderer
from pyprofile.runner import Runner

if __name__ == '__main__':
    runner = Runner(
        input_dir=Path('input'),
        output_dir=Path('output'),
        renderers=[
            CVRenderer(
                name='cv_theo_windebank.pdf',
                censor=False,
                exclude_experience=[]
            )
        ])
    runner.render()
