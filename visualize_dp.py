class SVGImage:
    def __init__(self):
        self.title = 'image'
        self.width = 800
        self.height = 800
        self.bgColor = '#2f3020'
        self.color = '#f2f2f2'

    def generate_header(self):
        content = f'''
        <svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">
        <g>
          <title>{self.title}</title>
          <rect fill="{self.bgColor}" id="canvas_background" height="{self.height}" width="{self.width}" y="0" x="0"/>
        </g>
        '''
        return content

    def generate_text(self, text, x, y, font_size=14):
        content = f'''
        <text font-weight="normal" xml:space="preserve" text-anchor="start"
          font-family="Courier New,Roboto Mono,Helvetica, Arial, sans-serif"
          font-size="{font_size}" y="{y}" x="{x}" stroke-width="0" stroke="#000" fill="{self.color}">
          {text}
        </text>
        '''
        return content

    def generate_body(self):
        content = f'''
        <g>
          <path d="M 115 380 Q 147 320, 180 380" stroke="#f2f2f2" fill="none"/>
          <path d="M 113 375 L 118 385 122 375z" stroke="#f2f2f2" fill="#f2f2f2"/>
        ''' + \
        self.generate_text('Theo Bloomberg, ông Joe Biden sẽ nhận nhiệm sở vào tháng tới', x=5, y=400) + \
        self.generate_text('obj', x=57, y=365, font_size=12) + \
        '''
        </g>
        '''
        return content

    def generate_footer(self):
        content = '''
        </svg>
        '''
        return content

    def draw(self):
        f = open('img.svg', 'w')
        content = self.generate_header()
        content += self.generate_body()
        content += self.generate_footer()
        f.write(content)
        f.close()


image = SVGImage()
image.draw()
