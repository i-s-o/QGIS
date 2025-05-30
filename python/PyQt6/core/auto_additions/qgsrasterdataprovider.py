# The following has been generated automatically from src/core/raster/qgsrasterdataprovider.h
QgsRasterDataProvider.TransformImageToLayer = QgsRasterDataProvider.TransformType.TransformImageToLayer
QgsRasterDataProvider.TransformLayerToImage = QgsRasterDataProvider.TransformType.TransformLayerToImage
try:
    QgsImageFetcher.__attribute_docs__ = {'finish': 'Emitted when the download completes\n\n:param legend: The downloaded legend image\n', 'progress': 'Emitted to report progress\n', 'error': 'Emitted when an error occurs\n'}
    QgsImageFetcher.__abstract_methods__ = ['start']
    QgsImageFetcher.__signal_arguments__ = {'finish': ['legend: QImage'], 'progress': ['received: int', 'total: int'], 'error': ['msg: str']}
    QgsImageFetcher.__group__ = ['raster']
except (NameError, AttributeError):
    pass
try:
    QgsRasterDataProvider.__attribute_docs__ = {'statusChanged': 'Emit a message to be displayed on status bar, usually used by network\nproviders (WMS,WCS)\n'}
    QgsRasterDataProvider.create = staticmethod(QgsRasterDataProvider.create)
    QgsRasterDataProvider.pyramidResamplingMethods = staticmethod(QgsRasterDataProvider.pyramidResamplingMethods)
    QgsRasterDataProvider.decodeVirtualRasterProviderUri = staticmethod(QgsRasterDataProvider.decodeVirtualRasterProviderUri)
    QgsRasterDataProvider.encodeVirtualRasterProviderUri = staticmethod(QgsRasterDataProvider.encodeVirtualRasterProviderUri)
    QgsRasterDataProvider.identifyFormatName = staticmethod(QgsRasterDataProvider.identifyFormatName)
    QgsRasterDataProvider.identifyFormatFromName = staticmethod(QgsRasterDataProvider.identifyFormatFromName)
    QgsRasterDataProvider.identifyFormatLabel = staticmethod(QgsRasterDataProvider.identifyFormatLabel)
    QgsRasterDataProvider.identifyFormatToCapability = staticmethod(QgsRasterDataProvider.identifyFormatToCapability)
    QgsRasterDataProvider.__virtual_methods__ = ['providerCapabilities', 'fields', 'colorInterpretation', 'reload', 'bandScale', 'bandOffset', 'maximumTileSize', 'sourceHasNoDataValue', 'useSourceNoDataValue', 'setUseSourceNoDataValue', 'sourceNoDataValue', 'setUserNoDataValue', 'userNoDataValues', 'colorTable', 'supportsLegendGraphic', 'getLegendGraphicFetcher', 'buildPyramids', 'buildPyramidList', 'identify', 'sample', 'lastErrorFormat', 'isEditable', 'setEditable', 'write', 'setNoDataValue', 'remove', 'validateCreationOptions', 'validatePyramidsConfigOptions', 'stepWidth', 'stepHeight', 'nativeResolutions', 'ignoreExtents', 'transformCoordinates', 'enableProviderResampling', 'setZoomedInResamplingMethod', 'setZoomedOutResamplingMethod', 'setMaxOversampling', 'writeNativeAttributeTable', 'readNativeAttributeTable', 'bandDescription']
    QgsRasterDataProvider.__abstract_methods__ = ['clone', 'extent', 'dataType', 'sourceDataType', 'lastErrorTitle', 'lastError']
    QgsRasterDataProvider.__overridden_methods__ = ['clone', 'setInput', 'extent', 'dataType', 'sourceDataType', 'colorInterpretationName', 'block', 'subLayers', 'temporalCapabilities', 'elevationProperties', 'timestamp', 'dataTimestamp', 'readXml', 'writeXml']
    QgsRasterDataProvider.__group__ = ['raster']
except (NameError, AttributeError):
    pass
try:
    QgsRasterDataProvider.VirtualRasterInputLayers.__doc__ = """Struct that stores information of the raster used in :py:class:`QgsVirtualRasterProvider` for the calculations,
this struct is  stored in the DecodedUriParameters

.. note::

   used by :py:class:`QgsVirtualRasterProvider` only"""
    QgsRasterDataProvider.VirtualRasterInputLayers.__group__ = ['raster']
except (NameError, AttributeError):
    pass
try:
    QgsRasterDataProvider.VirtualRasterParameters.__doc__ = """Struct that stores the information about the parameters that should be given to the
:py:class:`QgsVirtualRasterProvider` through the :py:class:`QgsRasterDataProvider`.DecodedUriParameters

.. note::

   used by :py:class:`QgsVirtualRasterProvider` only"""
    QgsRasterDataProvider.VirtualRasterParameters.__group__ = ['raster']
except (NameError, AttributeError):
    pass
