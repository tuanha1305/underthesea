class SVGImage:
    def __init__(self):
        self.title = 'image'
        self.width = 1600
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
        text = text.replace(" ", "&#160;")
        content = f'''
        <text font-weight="normal"
          text-anchor="start"
          white-space="pre"
          font-family="Courier New,Roboto Mono,Helvetica, Arial, sans-serif"
          font-size="{font_size}" y="{y}" x="{x}" stroke-width="0" stroke="#000" fill="{self.color}">
          {text}
        </text>
        '''
        return content

    def generate_body(self, nodes):
        content = f'''
        <g>
          <path d="M 115 380 Q 147 320, 180 380" stroke="#f2f2f2" fill="none"/>
          <path d="M 113 375 L 118 385 122 375z" stroke="#f2f2f2" fill="#f2f2f2"/>
        '''
        # node_positions = []
        x_pos = 20
        CHARACTER_WIDTH = 7
        TOKEN_SPACE_WIDTH = 40
        text_length = 0
        for node in nodes:
            text, pos, dep_rel, dep_type = node
            content += self.generate_text(text, x=x_pos, y=400)
            text_length += len(text)
            x_pos = x_pos + CHARACTER_WIDTH * len(text) + TOKEN_SPACE_WIDTH
        # content += self.generate_text('obj', x=57, y=365, font_size=12)
        content += '''
        </g>
        '''
        return content

    def generate_footer(self):
        content = '''
        </svg>
        '''
        return content

    def draw(self, nodes):
        f = open('img.svg', 'w')
        content = self.generate_header()
        content += self.generate_body(nodes)
        content += self.generate_footer()
        f.write(content)
        f.close()


text = 'Theo Bloomberg, ông Joe Biden sẽ nhận    nhiệm sở vào        tháng tới với nhiều đòn bẩy hơn để đối phó với Trung Quốc. '
nodes = [('Theo', 'V', 7, 'advcl'),
         ('Bloomberg', 'Np', 1, 'obj'),
         (',', 'CH', 1, 'punct'),
         ('ông', 'Nc', 5, 'det:clf'),
         ('Joe Biden', 'Np', 7, 'nsubj'),
         ('sẽ', 'R', 7, 'advmod'),
         ('nhận', 'V', 0, 'root'),
         ('nhiệm sở', 'V', 7, 'obj'),
         ('vào', 'E', 10, 'case'),
         ('tháng', 'N', 7, 'obl:tmod'),
         ('tới', 'V', 10, 'acl'),
         ('với', 'E', 14, 'case'),
         ('nhiều', 'A', 14, 'advmod:adj'),
         ('đòn bẩy', 'N', 11, 'obl'),
         ('hơn', 'A', 14, 'advmod:adj'),
         ('để', 'E', 17, 'mark:pcomp'),
         ('đối phó', 'V', 7, 'advcl:objective'),
         ('với', 'E', 19, 'case'),
         ('Trung Quốc', 'Np', 17, 'obl:with'),
         ('.', 'CH', 7, 'punct')]
image = SVGImage()
image.draw(nodes)
