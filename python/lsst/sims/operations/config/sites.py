import lsst.pex.config as pexConfig

from .base import siteconf as baseSite
import factories

@pexConfig.registerConfig("CerroPachon", factories.siteRegistry,
                          baseSite.SiteConfig)
class CerroPachon(baseSite.SiteConfig):
    """
    This is the concrete class holding all the information for the Cerro Pachon
    telescope site.
    """

    def setDefaults(self):
        """
        This function sets the defaults for the site.
        """
        self.name = "Cerro Pachon"
        self.seeingEpoch = 49353
        self.latitude = -29.666667
        self.longitude = -70.59
        self.height = 2737.0
        self.pressure = 1010.0
        self.temperature = 12.0
        self.relativeHumidity = 0.0
        self.weatherSeeingFudge = 1.0
        self.seeingTbl = "Seeing"
        self.cloudTbl = "Cloud"
