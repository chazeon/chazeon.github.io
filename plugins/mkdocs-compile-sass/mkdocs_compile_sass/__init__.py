from tempfile import TemporaryDirectory
from pathlib import Path
from mkdocs import plugins
import sass

from logging import getLogger

logger = getLogger("mkdocs")

class CompileSASSPlugin(plugins.BasePlugin):

    def __init__(self) -> None:

        super().__init__()
        self.temp_dir = TemporaryDirectory()

    def on_files(self, files, config):
        """Build our precious SCSS"""

        # dirs = [Path(d) for d in config["theme"]["dirs"]]

        temp_dir = Path(str(self.temp_dir.name))

        for file in files._files:

            src_path = Path(file.src_path)

            if src_path.suffix not in (".scss", ".sass"): continue

            css_path = temp_dir / src_path.parent / f"{src_path.stem}"
            css_path.parent.mkdir(parents=True, exist_ok=True)

            logger.info(f"Compiling SCSS <{src_path}> -> <{css_path}>")
            with open(css_path, "w", encoding="utf8") as fp:
                fp.write(sass.compile(filename=file.abs_src_path))
            
            file.name = str(Path(file.name).stem)

            file.src_path = str(css_path.relative_to(temp_dir))
            file.abs_src_path = str(css_path)
            file.dest_path = str(Path(file.dest_path).parent / Path(file.dest_path).name)
            file.abs_dest_path = str(Path(file.abs_dest_path).parent / Path(file.abs_dest_path).name)

            file.url = str(Path(file.url).parent / Path(file.url).name)

        return files
    
    def on_post_build(self, config):
        self.temp_dir.cleanup()