# encoding: utf-8
# module Grasshopper.GUI.HTML calls itself HTML
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_CssConstants(object):
    """ GH_CssConstants() """
    BlockChapter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockChapter(self: GH_CssConstants) -> GH_CssStyle

"""

    BlockContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockContent(self: GH_CssConstants) -> GH_CssStyle

"""

    BlockListTight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockListTight(self: GH_CssConstants) -> GH_CssStyle

"""

    BlockParagraph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockParagraph(self: GH_CssConstants) -> GH_CssStyle

"""

    BlockSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockSection(self: GH_CssConstants) -> GH_CssStyle

"""

    BlockSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockSeparator(self: GH_CssConstants) -> GH_CssStyle

"""

    BlockTight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockTight(self: GH_CssConstants) -> GH_CssStyle

"""

    ColourBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourBackground(self: GH_CssConstants) -> Color

Set: ColourBackground(self: GH_CssConstants) = value
"""

    ColourChapterBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourChapterBackground(self: GH_CssConstants) -> Color

Set: ColourChapterBackground(self: GH_CssConstants) = value
"""

    ColourFakeFaint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourFakeFaint(self: GH_CssConstants) -> Color

Set: ColourFakeFaint(self: GH_CssConstants) = value
"""

    ColourForeground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourForeground(self: GH_CssConstants) -> Color

Set: ColourForeground(self: GH_CssConstants) = value
"""

    ColourSectionBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColourSectionBackground(self: GH_CssConstants) -> Color

Set: ColourSectionBackground(self: GH_CssConstants) = value
"""

    Default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Default(self: GH_CssConstants) -> GH_CssStyle

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: GH_CssConstants) -> GH_CssStyle

"""

    TextChapter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextChapter(self: GH_CssConstants) -> GH_CssStyle

"""

    TextFaint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFaint(self: GH_CssConstants) -> GH_CssStyle

"""

    TextFaintCheat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFaintCheat(self: GH_CssConstants) -> GH_CssStyle

"""

    TextMonospace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextMonospace(self: GH_CssConstants) -> GH_CssStyle

"""

    TextParagraph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextParagraph(self: GH_CssConstants) -> GH_CssStyle

"""

    TextSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextSection(self: GH_CssConstants) -> GH_CssStyle

"""



class GH_CssProperty(object, IComparable[GH_CssProperty]):
    """
    GH_CssProperty(property: str)
    GH_CssProperty(property: str, value: str)
    GH_CssProperty(property: str, values: IEnumerable[str])
    """
    def AddValue(self, value):
        """ AddValue(self: GH_CssProperty, value: str) """
        pass

    def AddValues(self, values):
        """ AddValues(self: GH_CssProperty, values: IEnumerable[str]) """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: GH_CssProperty, other: GH_CssProperty) -> int """
        pass

    def FormatCss(self, indent):
        """ FormatCss(self: GH_CssProperty, indent: int) -> str """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, property, *__args):
        """
        __new__(cls: type, property: str)
        __new__(cls: type, property: str, value: str)
        __new__(cls: type, property: str, values: IEnumerable[str])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_CssProperty) -> str

"""

    ValueCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueCount(self: GH_CssProperty) -> int

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: GH_CssProperty) -> ReadOnlyCollection[str]

"""



class GH_CssStyle(object, IComparable[GH_CssStyle]):
    """
    GH_CssStyle()
    GH_CssStyle(selector: str)
    GH_CssStyle(selector: str, property: GH_CssProperty)
    GH_CssStyle(selector: str, properties: IEnumerable[GH_CssProperty])
    """
    def AddComment(self, comment):
        """ AddComment(self: GH_CssStyle, comment: str) """
        pass

    def AddProperty(self, *__args):
        """ AddProperty(self: GH_CssStyle, name: str, value: str)AddProperty(self: GH_CssStyle, property: GH_CssProperty) """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: GH_CssStyle, other: GH_CssStyle) -> int """
        pass

    def FormatCss(self, indent):
        """ FormatCss(self: GH_CssStyle, indent: int) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, selector=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, selector: str)
        __new__(cls: type, selector: str, property: GH_CssProperty)
        __new__(cls: type, selector: str, properties: IEnumerable[GH_CssProperty])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comments(self: GH_CssStyle) -> ReadOnlyCollection[str]

"""

    IsClassSelector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClassSelector(self: GH_CssStyle) -> bool

"""

    IsIdSelector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIdSelector(self: GH_CssStyle) -> bool

"""

    IsPluralSelector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPluralSelector(self: GH_CssStyle) -> bool

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Properties(self: GH_CssStyle) -> ReadOnlyCollection[GH_CssProperty]

"""

    Selector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selector(self: GH_CssStyle) -> str

Set: Selector(self: GH_CssStyle) = value
"""



class GH_CssStyleSheet(object):
    """ GH_CssStyleSheet() """
    def AddStyle(self, styles):
        """ AddStyle(self: GH_CssStyleSheet, *styles: Array[GH_CssStyle]) """
        pass

    def FormatCss(self, indent):
        """ FormatCss(self: GH_CssStyleSheet, indent: int) -> str """
        pass

    def IsStyleDefined(self, style):
        """ IsStyleDefined(self: GH_CssStyleSheet, style: GH_CssStyle) -> bool """
        pass

    Links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Links(self: GH_CssStyleSheet) -> ReadOnlyCollection[str]

"""

    Styles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Styles(self: GH_CssStyleSheet) -> ReadOnlyCollection[GH_CssStyle]

"""



class GH_HtmlFormatter(object):
    """
    GH_HtmlFormatter()
    GH_HtmlFormatter(nSource: IGH_InstanceDescription)
    GH_HtmlFormatter(nSource: IGH_InstanceDescription, nTitle: str)
    GH_HtmlFormatter(nSource: IGH_InstanceDescription, nTitle: str, nDescription: str)
    """
    def AddRemark(self, text, forecolour, backcolour):
        """ AddRemark(self: GH_HtmlFormatter, text: str, forecolour: GH_HtmlFormatterPalette, backcolour: GH_HtmlFormatterPalette) """
        pass

    def HtmlFormat(self):
        """ HtmlFormat(self: GH_HtmlFormatter) -> str """
        pass

    @staticmethod
    def HtmlPaletteTag(palette):
        """ HtmlPaletteTag(palette: GH_HtmlFormatterPalette) -> str """
        pass

    @staticmethod
    def ReplaceBoxDrawingCodes(source):
        """ ReplaceBoxDrawingCodes(source: str) -> str """
        pass

    @staticmethod
    def ReplaceSpecialCharCodes(source):
        """ ReplaceSpecialCharCodes(source: str) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nSource=None, nTitle=None, nDescription=None):
        """
        __new__(cls: type)
        __new__(cls: type, nSource: IGH_InstanceDescription)
        __new__(cls: type, nSource: IGH_InstanceDescription, nTitle: str)
        __new__(cls: type, nSource: IGH_InstanceDescription, nTitle: str, nDescription: str)
        """
        pass

    ContactURI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContactURI(self: GH_HtmlFormatter) -> str

Set: ContactURI(self: GH_HtmlFormatter) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_HtmlFormatter) -> str

Set: Description(self: GH_HtmlFormatter) = value
"""

    Remarks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Remarks(self: GH_HtmlFormatter) -> List[GH_HtmlRemark]

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: GH_HtmlFormatter) -> str

Set: Title(self: GH_HtmlFormatter) = value
"""

    WebPageURI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebPageURI(self: GH_HtmlFormatter) -> str

Set: WebPageURI(self: GH_HtmlFormatter) = value
"""


    m_description = None
    m_link_contact = None
    m_link_webpage = None
    m_remarks = None
    m_source = None
    m_title = None


class GH_HtmlFormatterPalette(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_HtmlFormatterPalette, values: Black (0), Blue (5), Cyan (7), Gray (1), Green (4), Magenta (8), Red (3), White (2), Yellow (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Black = None
    Blue = None
    Cyan = None
    Gray = None
    Green = None
    Magenta = None
    Red = None
    value__ = None
    White = None
    Yellow = None


class GH_HtmlHelpPopup(Form, IComponent, IDisposable, IOleControl, IOleObject, IOleInPlaceObject, IOleInPlaceActiveObject, IOleWindow, IViewObject, IViewObject2, IPersist, IPersistStreamInit, IPersistPropertyBag, IPersistStorage, IQuickActivate, ISupportOleDropSource, IDropTarget, ISynchronizeInvoke, IWin32Window, IArrangedElement, IBindableComponent, IContainerControl):
    """ GH_HtmlHelpPopup() """
    def AccessibilityNotifyClients(self, *args): #cannot find CLR method
        """
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, objectID: int, childID: int)
            Notifies the accessibility client applications of the specified 
             System.Windows.Forms.AccessibleEvents for the specified child control .
        
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            objectID: The identifier of the System.Windows.Forms.AccessibleObject.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, childID: int)
            Notifies the accessibility client applications of the specified 
             System.Windows.Forms.AccessibleEvents for the specified child control.
        
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        """
        pass

    def ActivateMdiChild(self, *args): #cannot find CLR method
        """
        ActivateMdiChild(self: Form, form: Form)
            Activates the MDI child of a form.
        
            form: The child form to activate.
        """
        pass

    def AdjustFormScrollbars(self, *args): #cannot find CLR method
        """
        AdjustFormScrollbars(self: Form, displayScrollbars: bool)
            Adjusts the scroll bars on the container based on the current control positions and the control 
             currently selected.
        
        
            displayScrollbars: true to show the scroll bars; otherwise, false.
        """
        pass

    def ApplyAutoScaling(self, *args): #cannot find CLR method
        """
        ApplyAutoScaling(self: Form)
            Resizes the form according to the current value of the 
             System.Windows.Forms.Form.AutoScaleBaseSize property and the size of the current font.
        """
        pass

    def CenterToParent(self, *args): #cannot find CLR method
        """
        CenterToParent(self: Form)
            Centers the position of the form within the bounds of the parent form.
        """
        pass

    def CenterToScreen(self, *args): #cannot find CLR method
        """
        CenterToScreen(self: Form)
            Centers the form on the current screen.
        """
        pass

    @staticmethod
    def CloseAllPopupDialogs():
        """ CloseAllPopupDialogs() """
        pass

    def CreateAccessibilityInstance(self, *args): #cannot find CLR method
        """
        CreateAccessibilityInstance(self: Control) -> AccessibleObject
        
            Creates a new accessibility object for the control.
            Returns: A new System.Windows.Forms.AccessibleObject for the control.
        """
        pass

    def CreateControlsInstance(self, *args): #cannot find CLR method
        """
        CreateControlsInstance(self: Form) -> ControlCollection
            Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to the control.
        """
        pass

    def CreateHandle(self, *args): #cannot find CLR method
        """
        CreateHandle(self: Form)
            Creates the handle for the form. If a derived class overrides this function, it must call the 
             base implementation.
        """
        pass

    def DefWndProc(self, *args): #cannot find CLR method
        """
        DefWndProc(self: Form, m: Message) -> Message
        
            m: The Windows System.Windows.Forms.Message to process.
        """
        pass

    def DestroyHandle(self, *args): #cannot find CLR method
        """
        DestroyHandle(self: Control)
            Destroys the handle associated with the control.
        """
        pass

    def Dispose(self):
        """ Dispose(self: GH_HtmlHelpPopup, disposing: bool) """
        pass

    def GetAccessibilityObjectById(self, *args): #cannot find CLR method
        """
        GetAccessibilityObjectById(self: Control, objectId: int) -> AccessibleObject
        
            Retrieves the specified System.Windows.Forms.AccessibleObject.
        
            objectId: An Int32 that identifies the System.Windows.Forms.AccessibleObject to retrieve.
            Returns: An System.Windows.Forms.AccessibleObject.
        """
        pass

    def GetAutoSizeMode(self, *args): #cannot find CLR method
        """
        GetAutoSizeMode(self: Control) -> AutoSizeMode
        
            Retrieves a value indicating how a control will behave when its 
             System.Windows.Forms.Control.AutoSize property is enabled.
        
            Returns: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def GetScaledBounds(self, *args): #cannot find CLR method
        """
        GetScaledBounds(self: Form, bounds: Rectangle, factor: SizeF, specified: BoundsSpecified) -> Rectangle
        
            bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.
            factor: The height and width of the control's bounds.
            specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the 
             control to use when defining its size and position.
        
            Returns: A System.Drawing.Rectangle representing the bounds within which the control is scaled.
        """
        pass

    def GetScrollState(self, *args): #cannot find CLR method
        """
        GetScrollState(self: ScrollableControl, bit: int) -> bool
        
            Determines whether the specified flag has been set.
        
            bit: The flag to check.
            Returns: true if the specified flag has been set; otherwise, false.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def GetStyle(self, *args): #cannot find CLR method
        """
        GetStyle(self: Control, flag: ControlStyles) -> bool
        
            Retrieves the value of the specified control style bit for the control.
        
            flag: The System.Windows.Forms.ControlStyles bit to return the value from.
            Returns: true if the specified control style bit is set to true; otherwise, false.
        """
        pass

    def GetTopLevel(self, *args): #cannot find CLR method
        """
        GetTopLevel(self: Control) -> bool
        
            Determines if the control is a top-level control.
            Returns: true if the control is a top-level control; otherwise, false.
        """
        pass

    def InitLayout(self, *args): #cannot find CLR method
        """
        InitLayout(self: Control)
            Called after the control has been added to another container.
        """
        pass

    def InvokeGotFocus(self, *args): #cannot find CLR method
        """
        InvokeGotFocus(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.GotFocus event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokeLostFocus(self, *args): #cannot find CLR method
        """
        InvokeLostFocus(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.LostFocus event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokeOnClick(self, *args): #cannot find CLR method
        """
        InvokeOnClick(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Click event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Click event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokePaint(self, *args): #cannot find CLR method
        """
        InvokePaint(self: Control, c: Control, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event for the specified control.
        
            c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event to.
            e: An System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def InvokePaintBackground(self, *args): #cannot find CLR method
        """
        InvokePaintBackground(self: Control, c: Control, e: PaintEventArgs)
            Raises the PaintBackground event for the specified control.
        
            c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event to.
            e: An System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def IsInputChar(self, *args): #cannot find CLR method
        """
        IsInputChar(self: Control, charCode: Char) -> bool
        
            Determines if a character is an input character that the control recognizes.
        
            charCode: The character to test.
            Returns: true if the character should be sent directly to the control and not preprocessed; otherwise, 
             false.
        """
        pass

    def IsInputKey(self, *args): #cannot find CLR method
        """
        IsInputKey(self: Control, keyData: Keys) -> bool
        
            Determines whether the specified key is a regular input key or a special key that requires 
             preprocessing.
        
        
            keyData: One of the System.Windows.Forms.Keys values.
            Returns: true if the specified key is a regular input key; otherwise, false.
        """
        pass

    def LoadHTML(self, syntax):
        """ LoadHTML(self: GH_HtmlHelpPopup, syntax: GH_HtmlFormatter)LoadHTML(self: GH_HtmlHelpPopup, syntax: str) """
        pass

    def LoadObject(self, obj):
        """ LoadObject(self: GH_HtmlHelpPopup, obj: GH_DocumentObject) -> bool """
        pass

    def LoadRemoteHTML(self, uri):
        """ LoadRemoteHTML(self: GH_HtmlHelpPopup, uri: str) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NotifyInvalidate(self, *args): #cannot find CLR method
        """
        NotifyInvalidate(self: Control, invalidatedArea: Rectangle)
            Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the control 
             to invalidate.
        
        
            invalidatedArea: A System.Drawing.Rectangle representing the area to invalidate.
        """
        pass

    def OnActivated(self, *args): #cannot find CLR method
        """
        OnActivated(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Activated event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnAutoSizeChanged(self, *args): #cannot find CLR method
        """
        OnAutoSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.AutoSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnAutoValidateChanged(self, *args): #cannot find CLR method
        """
        OnAutoValidateChanged(self: ContainerControl, e: EventArgs)
            Raises the System.Windows.Forms.ContainerControl.AutoValidateChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBackColorChanged(self, *args): #cannot find CLR method
        """
        OnBackColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackColorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBackgroundImageChanged(self, *args): #cannot find CLR method
        """
        OnBackgroundImageChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event.
        
            e: An System.EventArgs that contains the data.
        """
        pass

    def OnBackgroundImageLayoutChanged(self, *args): #cannot find CLR method
        """
        OnBackgroundImageLayoutChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageLayoutChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBindingContextChanged(self, *args): #cannot find CLR method
        """
        OnBindingContextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BindingContextChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnCausesValidationChanged(self, *args): #cannot find CLR method
        """
        OnCausesValidationChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CausesValidationChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnChangeUICues(self, *args): #cannot find CLR method
        """
        OnChangeUICues(self: Control, e: UICuesEventArgs)
            Raises the System.Windows.Forms.Control.ChangeUICues event.
        
            e: A System.Windows.Forms.UICuesEventArgs that contains the event data.
        """
        pass

    def OnClick(self, *args): #cannot find CLR method
        """
        OnClick(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Click event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnClientSizeChanged(self, *args): #cannot find CLR method
        """
        OnClientSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ClientSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnClosed(self, *args): #cannot find CLR method
        """
        OnClosed(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Closed event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnClosing(self, *args): #cannot find CLR method
        """
        OnClosing(self: Form, e: CancelEventArgs)
            Raises the System.Windows.Forms.Form.Closing event.
        
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        pass

    def OnContextMenuChanged(self, *args): #cannot find CLR method
        """
        OnContextMenuChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ContextMenuChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnContextMenuStripChanged(self, *args): #cannot find CLR method
        """
        OnContextMenuStripChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ContextMenuStripChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnControlAdded(self, *args): #cannot find CLR method
        """
        OnControlAdded(self: Control, e: ControlEventArgs)
            Raises the System.Windows.Forms.Control.ControlAdded event.
        
            e: A System.Windows.Forms.ControlEventArgs that contains the event data.
        """
        pass

    def OnControlRemoved(self, *args): #cannot find CLR method
        """
        OnControlRemoved(self: Control, e: ControlEventArgs)
            Raises the System.Windows.Forms.Control.ControlRemoved event.
        
            e: A System.Windows.Forms.ControlEventArgs that contains the event data.
        """
        pass

    def OnCreateControl(self, *args): #cannot find CLR method
        """
        OnCreateControl(self: Form)
            Raises the CreateControl event.
        """
        pass

    def OnCursorChanged(self, *args): #cannot find CLR method
        """
        OnCursorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CursorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDeactivate(self, *args): #cannot find CLR method
        """
        OnDeactivate(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Deactivate event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnDockChanged(self, *args): #cannot find CLR method
        """
        OnDockChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.DockChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDoubleClick(self, *args): #cannot find CLR method
        """
        OnDoubleClick(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.DoubleClick event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Form, e: DpiChangedEventArgs) """
        pass

    def OnDpiChangedAfterParent(self, *args): #cannot find CLR method
        """ OnDpiChangedAfterParent(self: Control, e: EventArgs) """
        pass

    def OnDpiChangedBeforeParent(self, *args): #cannot find CLR method
        """ OnDpiChangedBeforeParent(self: Control, e: EventArgs) """
        pass

    def OnDragDrop(self, *args): #cannot find CLR method
        """
        OnDragDrop(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragDrop event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragEnter event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.DragLeave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragOver event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnEnabledChanged(self, *args): #cannot find CLR method
        """
        OnEnabledChanged(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnEnter(self, *args): #cannot find CLR method
        """
        OnEnter(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Control.Enter event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnFontChanged(self, *args): #cannot find CLR method
        """
        OnFontChanged(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnForeColorChanged(self, *args): #cannot find CLR method
        """
        OnForeColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ForeColorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnFormClosed(self, *args): #cannot find CLR method
        """
        OnFormClosed(self: Form, e: FormClosedEventArgs)
            Raises the System.Windows.Forms.Form.FormClosed event.
        
            e: A System.Windows.Forms.FormClosedEventArgs that contains the event data.
        """
        pass

    def OnFormClosing(self, *args): #cannot find CLR method
        """
        OnFormClosing(self: Form, e: FormClosingEventArgs)
            Raises the System.Windows.Forms.Form.FormClosing event.
        
            e: A System.Windows.Forms.FormClosingEventArgs that contains the event data.
        """
        pass

    def OnGetDpiScaledSize(self, *args): #cannot find CLR method
        """ OnGetDpiScaledSize(self: Form, deviceDpiOld: int, deviceDpiNew: int, desiredSize: Size) -> (bool, Size) """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: Control, gfbevent: GiveFeedbackEventArgs)
            Raises the System.Windows.Forms.Control.GiveFeedback event.
        
            gfbevent: A System.Windows.Forms.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.GotFocus event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHandleCreated(self, *args): #cannot find CLR method
        """
        OnHandleCreated(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHandleDestroyed(self, *args): #cannot find CLR method
        """
        OnHandleDestroyed(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHelpButtonClicked(self, *args): #cannot find CLR method
        """
        OnHelpButtonClicked(self: Form, e: CancelEventArgs)
            Raises the System.Windows.Forms.Form.HelpButtonClicked event.
        
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        pass

    def OnHelpRequested(self, *args): #cannot find CLR method
        """
        OnHelpRequested(self: Control, hevent: HelpEventArgs)
            Raises the System.Windows.Forms.Control.HelpRequested event.
        
            hevent: A System.Windows.Forms.HelpEventArgs that contains the event data.
        """
        pass

    def OnImeModeChanged(self, *args): #cannot find CLR method
        """
        OnImeModeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ImeModeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnInputLanguageChanged(self, *args): #cannot find CLR method
        """
        OnInputLanguageChanged(self: Form, e: InputLanguageChangedEventArgs)
            Raises the System.Windows.Forms.Form.InputLanguageChanged event.
        
            e: The System.Windows.Forms.InputLanguageChangedEventArgs that contains the event data.
        """
        pass

    def OnInputLanguageChanging(self, *args): #cannot find CLR method
        """
        OnInputLanguageChanging(self: Form, e: InputLanguageChangingEventArgs)
            Raises the System.Windows.Forms.Form.InputLanguageChanging event.
        
            e: The System.Windows.Forms.InputLanguageChangingEventArgs that contains the event data.
        """
        pass

    def OnInvalidated(self, *args): #cannot find CLR method
        """
        OnInvalidated(self: Control, e: InvalidateEventArgs)
            Raises the System.Windows.Forms.Control.Invalidated event.
        
            e: An System.Windows.Forms.InvalidateEventArgs that contains the event data.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: Control, e: KeyEventArgs)
            Raises the System.Windows.Forms.Control.KeyDown event.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def OnKeyPress(self, *args): #cannot find CLR method
        """
        OnKeyPress(self: Control, e: KeyPressEventArgs)
            Raises the System.Windows.Forms.Control.KeyPress event.
        
            e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: Control, e: KeyEventArgs)
            Raises the System.Windows.Forms.Control.KeyUp event.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def OnLayout(self, *args): #cannot find CLR method
        """
        OnLayout(self: Form, levent: LayoutEventArgs)
            Raises the System.Windows.Forms.Control.Layout event.
        
            levent: The event data.
        """
        pass

    def OnLeave(self, *args): #cannot find CLR method
        """
        OnLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Leave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLoad(self, *args): #cannot find CLR method
        """
        OnLoad(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Load event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLocationChanged(self, *args): #cannot find CLR method
        """
        OnLocationChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.LocationChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.LostFocus event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMarginChanged(self, *args): #cannot find CLR method
        """
        OnMarginChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MarginChanged event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnMaximizedBoundsChanged(self, *args): #cannot find CLR method
        """
        OnMaximizedBoundsChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MaximizedBoundsChanged event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMaximumSizeChanged(self, *args): #cannot find CLR method
        """
        OnMaximumSizeChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MaximumSizeChanged event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMdiChildActivate(self, *args): #cannot find CLR method
        """
        OnMdiChildActivate(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MdiChildActivate event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMenuComplete(self, *args): #cannot find CLR method
        """
        OnMenuComplete(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MenuComplete event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMenuStart(self, *args): #cannot find CLR method
        """
        OnMenuStart(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MenuStart event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMinimumSizeChanged(self, *args): #cannot find CLR method
        """
        OnMinimumSizeChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MinimumSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseCaptureChanged(self, *args): #cannot find CLR method
        """
        OnMouseCaptureChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseCaptureChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseClick(self, *args): #cannot find CLR method
        """
        OnMouseClick(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseClick event.
        
            e: An System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnMouseDoubleClick(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseDoubleClick event.
        
            e: An System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseDown event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseEnter event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseHover(self, *args): #cannot find CLR method
        """
        OnMouseHover(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseHover event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseLeave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseMove event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseUp event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: ScrollableControl, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseWheel event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMove(self, *args): #cannot find CLR method
        """
        OnMove(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Move event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnNotifyMessage(self, *args): #cannot find CLR method
        """
        OnNotifyMessage(self: Control, m: Message)
            Notifies the control of Windows messages.
        
            m: A System.Windows.Forms.Message that represents the Windows message.
        """
        pass

    def OnPaddingChanged(self, *args): #cannot find CLR method
        """
        OnPaddingChanged(self: ScrollableControl, e: EventArgs)
            Raises the System.Windows.Forms.Control.PaddingChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPaint(self, *args): #cannot find CLR method
        """
        OnPaint(self: Form, e: PaintEventArgs)
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnPaintBackground(self, *args): #cannot find CLR method
        """
        OnPaintBackground(self: ScrollableControl, e: PaintEventArgs)
            Paints the background of the control.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnParentBackColorChanged(self, *args): #cannot find CLR method
        """
        OnParentBackColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackColorChanged event when the 
             System.Windows.Forms.Control.BackColor property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBackgroundImageChanged(self, *args): #cannot find CLR method
        """
        OnParentBackgroundImageChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event when the 
             System.Windows.Forms.Control.BackgroundImage property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBindingContextChanged(self, *args): #cannot find CLR method
        """
        OnParentBindingContextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BindingContextChanged event when the 
             System.Windows.Forms.Control.BindingContext property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentChanged(self, *args): #cannot find CLR method
        """
        OnParentChanged(self: ContainerControl, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentCursorChanged(self, *args): #cannot find CLR method
        """
        OnParentCursorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CursorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentEnabledChanged(self, *args): #cannot find CLR method
        """
        OnParentEnabledChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.EnabledChanged event when the 
             System.Windows.Forms.Control.Enabled property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentFontChanged(self, *args): #cannot find CLR method
        """
        OnParentFontChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.FontChanged event when the 
             System.Windows.Forms.Control.Font property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentForeColorChanged(self, *args): #cannot find CLR method
        """
        OnParentForeColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ForeColorChanged event when the 
             System.Windows.Forms.Control.ForeColor property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnParentRightToLeftChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RightToLeftChanged event when the 
             System.Windows.Forms.Control.RightToLeft property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentVisibleChanged(self, *args): #cannot find CLR method
        """
        OnParentVisibleChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.VisibleChanged event when the 
             System.Windows.Forms.Control.Visible property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: Control, e: PreviewKeyDownEventArgs)
            Raises the System.Windows.Forms.Control.PreviewKeyDown event.
        
            e: A System.Windows.Forms.PreviewKeyDownEventArgs that contains the event data.
        """
        pass

    def OnPrint(self, *args): #cannot find CLR method
        """
        OnPrint(self: Control, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: Control, qcdevent: QueryContinueDragEventArgs)
            Raises the System.Windows.Forms.Control.QueryContinueDrag event.
        
            qcdevent: A System.Windows.Forms.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnRegionChanged(self, *args): #cannot find CLR method
        """
        OnRegionChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RegionChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnResize(self, *args): #cannot find CLR method
        """
        OnResize(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnResizeBegin(self, *args): #cannot find CLR method
        """
        OnResizeBegin(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.ResizeBegin event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnResizeEnd(self, *args): #cannot find CLR method
        """
        OnResizeEnd(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.ResizeEnd event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnRightToLeftChanged(self: ScrollableControl, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnRightToLeftLayoutChanged(self, *args): #cannot find CLR method
        """
        OnRightToLeftLayoutChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.RightToLeftLayoutChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnScroll(self, *args): #cannot find CLR method
        """
        OnScroll(self: ScrollableControl, se: ScrollEventArgs)
            Raises the System.Windows.Forms.ScrollableControl.Scroll event.
        
            se: A System.Windows.Forms.ScrollEventArgs that contains the event data.
        """
        pass

    def OnShown(self, *args): #cannot find CLR method
        """
        OnShown(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Shown event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnSizeChanged(self, *args): #cannot find CLR method
        """
        OnSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.SizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnSystemColorsChanged(self, *args): #cannot find CLR method
        """
        OnSystemColorsChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.SystemColorsChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTabIndexChanged(self, *args): #cannot find CLR method
        """
        OnTabIndexChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.TabIndexChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTabStopChanged(self, *args): #cannot find CLR method
        """
        OnTabStopChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.TabStopChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTextChanged(self, *args): #cannot find CLR method
        """
        OnTextChanged(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnValidated(self, *args): #cannot find CLR method
        """
        OnValidated(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Validated event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnValidating(self, *args): #cannot find CLR method
        """
        OnValidating(self: Control, e: CancelEventArgs)
            Raises the System.Windows.Forms.Control.Validating event.
        
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        pass

    def OnVisibleChanged(self, *args): #cannot find CLR method
        """
        OnVisibleChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Control.VisibleChanged event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def ProcessCmdKey(self, *args): #cannot find CLR method
        """
        ProcessCmdKey(self: Form, msg: Message, keyData: Keys) -> (bool, Message)
        
            Processes a command key.
        
            msg: A System.Windows.Forms.Message, passed by reference, that represents the Win32 message to 
             process.
        
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the keystroke was processed and consumed by the control; otherwise, false to allow 
             further processing.
        """
        pass

    def ProcessDialogChar(self, *args): #cannot find CLR method
        """
        ProcessDialogChar(self: Form, charCode: Char) -> bool
        
            Processes a dialog character.
        
            charCode: The character to process.
            Returns: true if the character was processed by the control; otherwise, false.
        """
        pass

    def ProcessDialogKey(self, *args): #cannot find CLR method
        """
        ProcessDialogKey(self: Form, keyData: Keys) -> bool
        
            Processes a dialog box key.
        
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the keystroke was processed and consumed by the control; otherwise, false to allow 
             further processing.
        """
        pass

    def ProcessKeyEventArgs(self, *args): #cannot find CLR method
        """
        ProcessKeyEventArgs(self: Control, m: Message) -> (bool, Message)
        
            Processes a key message and generates the appropriate control events.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyMessage(self, *args): #cannot find CLR method
        """
        ProcessKeyMessage(self: Control, m: Message) -> (bool, Message)
        
            Processes a keyboard message.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyPreview(self, *args): #cannot find CLR method
        """
        ProcessKeyPreview(self: Form, m: Message) -> (bool, Message)
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessMnemonic(self, *args): #cannot find CLR method
        """
        ProcessMnemonic(self: Form, charCode: Char) -> bool
        
            Processes a mnemonic character.
        
            charCode: The character to process.
            Returns: true if the character was processed as a mnemonic by the control; otherwise, false.
        """
        pass

    def ProcessTabKey(self, *args): #cannot find CLR method
        """
        ProcessTabKey(self: Form, forward: bool) -> bool
        
            forward: true to cycle forward through the controls in the System.Windows.Forms.ContainerControl; 
             otherwise, false.
        
            Returns: true if a control is selected; otherwise, false.
        """
        pass

    def RaiseDragEvent(self, *args): #cannot find CLR method
        """
        RaiseDragEvent(self: Control, key: object, e: DragEventArgs)
            Raises the appropriate drag event.
        
            key: The event to raise.
            e: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def RaiseKeyEvent(self, *args): #cannot find CLR method
        """
        RaiseKeyEvent(self: Control, key: object, e: KeyEventArgs)
            Raises the appropriate key event.
        
            key: The event to raise.
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def RaiseMouseEvent(self, *args): #cannot find CLR method
        """
        RaiseMouseEvent(self: Control, key: object, e: MouseEventArgs)
            Raises the appropriate mouse event.
        
            key: The event to raise.
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def RaisePaintEvent(self, *args): #cannot find CLR method
        """
        RaisePaintEvent(self: Control, key: object, e: PaintEventArgs)
            Raises the appropriate paint event.
        
            key: The event to raise.
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def RecreateHandle(self, *args): #cannot find CLR method
        """
        RecreateHandle(self: Control)
            Forces the re-creation of the handle for the control.
        """
        pass

    def Register(self, *args): #cannot find CLR method
        """ Register(nForm: GH_HtmlHelpPopup) """
        pass

    def RescaleConstantsForDpi(self, *args): #cannot find CLR method
        """ RescaleConstantsForDpi(self: Control, deviceDpiOld: int, deviceDpiNew: int) """
        pass

    def ResetMouseEventArgs(self, *args): #cannot find CLR method
        """
        ResetMouseEventArgs(self: Control)
            Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
        """
        pass

    def RtlTranslateAlignment(self, *args): #cannot find CLR method
        """
        RtlTranslateAlignment(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate 
             System.Drawing.ContentAlignment to support right-to-left text.
        
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        RtlTranslateAlignment(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 
             System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        RtlTranslateAlignment(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 
             System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateContent(self, *args): #cannot find CLR method
        """
        RtlTranslateContent(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate 
             System.Drawing.ContentAlignment to support right-to-left text.
        
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        """
        pass

    def RtlTranslateHorizontal(self, *args): #cannot find CLR method
        """
        RtlTranslateHorizontal(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 
             System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateLeftRight(self, *args): #cannot find CLR method
        """
        RtlTranslateLeftRight(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 
             System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        """
        pass

    def ScaleControl(self, *args): #cannot find CLR method
        """
        ScaleControl(self: Form, factor: SizeF, specified: BoundsSpecified)
            Scales the location, size, padding, and margin of a control.
        
            factor: The factor by which the height and width of the control are scaled.
            specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to use 
             when defining its size and position.
        """
        pass

    def ScaleCore(self, *args): #cannot find CLR method
        """
        ScaleCore(self: Form, x: Single, y: Single)
            Performs scaling of the form.
        
            x: Percentage to scale the form horizontally
            y: Percentage to scale the form vertically
        """
        pass

    def ScrollToControl(self, *args): #cannot find CLR method
        """
        ScrollToControl(self: ScrollableControl, activeControl: Control) -> Point
        
            Calculates the scroll offset to the specified child control.
        
            activeControl: The child control to scroll into view.
            Returns: The upper-left hand System.Drawing.Point of the display area relative to the client area 
             required to scroll the control into view.
        """
        pass

    def Select(self):
        """
        Select(self: Form, directed: bool, forward: bool)
            Selects this form, and optionally selects the next or previous control.
        
            directed: If set to true that the active control is changed
            forward: If directed is true, then this controls the direction in which focus is moved. If this is true, 
             then the next control is selected; otherwise, the previous control is selected.
        """
        pass

    def SetAutoSizeMode(self, *args): #cannot find CLR method
        """
        SetAutoSizeMode(self: Control, mode: AutoSizeMode)
            Sets a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize 
             property is enabled.
        
        
            mode: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def SetBoundsCore(self, *args): #cannot find CLR method
        """
        SetBoundsCore(self: Form, x: int, y: int, width: int, height: int, specified: BoundsSpecified)
            x: The x-coordinate.
            y: The y-coordinate.
            width: The bounds width.
            height: The bounds height.
            specified: A value from the BoundsSpecified enumeration.
        """
        pass

    def SetClientSizeCore(self, *args): #cannot find CLR method
        """
        SetClientSizeCore(self: Form, x: int, y: int)
            Sets the client size of the form. This will adjust the bounds of the form to make the client 
             size the requested size.
        
        
            x: Requested width of the client region.
            y: Requested height of the client region.
        """
        pass

    def SetDisplayRectLocation(self, *args): #cannot find CLR method
        """
        SetDisplayRectLocation(self: ScrollableControl, x: int, y: int)
            Positions the display window to the specified value.
        
            x: The horizontal offset at which to position the System.Windows.Forms.ScrollableControl.
            y: The vertical offset at which to position the System.Windows.Forms.ScrollableControl.
        """
        pass

    def SetLocation(self, pt):
        """ SetLocation(self: GH_HtmlHelpPopup, pt: Point) """
        pass

    def SetScrollState(self, *args): #cannot find CLR method
        """
        SetScrollState(self: ScrollableControl, bit: int, value: bool)
            Sets the specified scroll state flag.
        
            bit: The scroll state flag to set.
            value: The value to set the flag.
        """
        pass

    def SetStyle(self, *args): #cannot find CLR method
        """
        SetStyle(self: Control, flag: ControlStyles, value: bool)
            Sets a specified System.Windows.Forms.ControlStyles flag to either true or false.
        
            flag: The System.Windows.Forms.ControlStyles bit to set.
            value: true to apply the specified style to the control; otherwise, false.
        """
        pass

    def SetTopLevel(self, *args): #cannot find CLR method
        """
        SetTopLevel(self: Control, value: bool)
            Sets the control as the top-level control.
        
            value: true to set the control as the top-level control; otherwise, false.
        """
        pass

    def SetVisibleCore(self, *args): #cannot find CLR method
        """
        SetVisibleCore(self: Form, value: bool)
            value: true to make the control visible; otherwise, false.
        """
        pass

    def SizeFromClientSize(self, *args): #cannot find CLR method
        """
        SizeFromClientSize(self: Control, clientSize: Size) -> Size
        
            Determines the size of the entire control from the height and width of its client area.
        
            clientSize: A System.Drawing.Size value representing the height and width of the control's client area.
            Returns: A System.Drawing.Size value representing the height and width of the entire control.
        """
        pass

    def UnRegister(self, *args): #cannot find CLR method
        """ UnRegister(nForm: GH_HtmlHelpPopup) """
        pass

    def UpdateBounds(self, *args): #cannot find CLR method
        """
        UpdateBounds(self: Control, x: int, y: int, width: int, height: int, clientWidth: int, clientHeight: int)
            Updates the bounds of the control with the specified size, location, and client size.
        
            x: The System.Drawing.Point.X coordinate of the control.
            y: The System.Drawing.Point.Y coordinate of the control.
            width: The System.Drawing.Size.Width of the control.
            height: The System.Drawing.Size.Height of the control.
            clientWidth: The client System.Drawing.Size.Width of the control.
            clientHeight: The client System.Drawing.Size.Height of the control.
        UpdateBounds(self: Control, x: int, y: int, width: int, height: int)
            Updates the bounds of the control with the specified size and location.
        
            x: The System.Drawing.Point.X coordinate of the control.
            y: The System.Drawing.Point.Y coordinate of the control.
            width: The System.Drawing.Size.Width of the control.
            height: The System.Drawing.Size.Height of the control.
        UpdateBounds(self: Control)
            Updates the bounds of the control with the current size and location.
        """
        pass

    def UpdateDefaultButton(self, *args): #cannot find CLR method
        """
        UpdateDefaultButton(self: Form)
            Updates which button is the default button.
        """
        pass

    def UpdateStyles(self, *args): #cannot find CLR method
        """
        UpdateStyles(self: Control)
            Forces the assigned styles to be reapplied to the control.
        """
        pass

    def UpdateZOrder(self, *args): #cannot find CLR method
        """
        UpdateZOrder(self: Control)
            Updates the control in its parent's z-order.
        """
        pass

    def WndProc(self, *args): #cannot find CLR method
        """
        WndProc(self: Form, m: Message) -> Message
        
            m: The Windows System.Windows.Forms.Message to process.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AutoScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the scaling factor between the current and design-time automatic scaling dimensions.

"""

    BrowserControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BrowserControl(self: GH_HtmlHelpPopup) -> WebBrowser

"""

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value, to enable IME support.

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if events can be raised on the control.

"""

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default cursor for the control.

"""

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default Input Method Editor (IME) mode supported by the control.

"""

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the space, in pixels, that is specified by default between controls.

"""

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default maximum size of a control.

"""

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default minimum size of a control.

"""

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the internal spacing, in pixels, of the contents of a control.

"""

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the font of the control.

"""

    HScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the horizontal scroll bar is visible.

"""

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the IME mode of a control.

"""

    MaximizedBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the size of the form when it is maximized.

"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is now obsolete.

"""

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the control redraws itself when resized.

"""

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines the scaling of child controls.

"""

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the control should display focus rectangles.

"""

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.

"""

    ShowWithoutActivation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the window will be activated when it is shown.

"""

    VScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the vertical scroll bar is visible.

"""


    m_Dragging = None
    m_DragStart = None
    m_FormStart = None
    m_help_forms = None
    RegisteredForms = None


class GH_HtmlListType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_HtmlListType, values: None (0), Ordered (2), Unordered (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    Ordered = None
    Unordered = None
    value__ = None


class GH_HtmlRemark(object):
    """ GH_HtmlRemark() """
    m_backcolour = None
    m_forecolour = None
    m_Text = None


class GH_HtmlTable(object):
    """
    GH_HtmlTable()
    GH_HtmlTable(rows: int, columns: int, FirstRowIsHeader: bool)
    """
    def FormatHtml(self):
        """ FormatHtml(self: GH_HtmlTable) -> str """
        pass

    def SetAllTextSizes(self, nSize):
        """ SetAllTextSizes(self: GH_HtmlTable, nSize: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, rows=None, columns=None, FirstRowIsHeader=None):
        """
        __new__(cls: type)
        __new__(cls: type, rows: int, columns: int, FirstRowIsHeader: bool)
        """
        pass

    Border = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Border(self: GH_HtmlTable) -> int

Set: Border(self: GH_HtmlTable) = value
"""

    Padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Padding(self: GH_HtmlTable) -> int

Set: Padding(self: GH_HtmlTable) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: GH_HtmlTable) -> int

Set: Width(self: GH_HtmlTable) = value
"""


    m_border = None
    m_padding = None
    m_rows = None
    m_width = None


class GH_HtmlTableRow(object):
    """ GH_HtmlTableRow(n_Cells: int) """
    def FormatHtml(self):
        """ FormatHtml(self: GH_HtmlTableRow) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, n_Cells):
        """ __new__(cls: type, n_Cells: int) """
        pass

    BackColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackColor(self: GH_HtmlTableRow) -> Color

Set: BackColor(self: GH_HtmlTableRow) = value
"""

    Bold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bold(self: GH_HtmlTableRow) -> bool

Set: Bold(self: GH_HtmlTableRow) = value
"""

    ForeColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForeColor(self: GH_HtmlTableRow) -> Color

Set: ForeColor(self: GH_HtmlTableRow) = value
"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Header(self: GH_HtmlTableRow) -> bool

Set: Header(self: GH_HtmlTableRow) = value
"""

    Italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Italic(self: GH_HtmlTableRow) -> bool

Set: Italic(self: GH_HtmlTableRow) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: GH_HtmlTableRow) -> int

Set: Size(self: GH_HtmlTableRow) = value
"""


    m_backcolor = None
    m_bold = None
    m_cells = None
    m_forecolor = None
    m_header = None
    m_italic = None
    m_size = None
    m_width = None


class GH_HtmlTextProperties(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) GH_HtmlTextProperties, values: Code (16), Emphasis (2), None (0), Strong (1), SubScript (8), SuperScript (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Code = None
    Emphasis = None
    None = None
    Strong = None
    SubScript = None
    SuperScript = None
    value__ = None


class GH_HtmlWriter(object):
    """
    GH_HtmlWriter()
    GH_HtmlWriter(*cssStyles: Array[GH_CssStyle])
    """
    def ComposeHTMLDocument(self, cssBodyStyles):
        """
        ComposeHTMLDocument(self: GH_HtmlWriter, *cssBodyStyles: Array[str]) -> str
        ComposeHTMLDocument(self: GH_HtmlWriter, *cssBodyStyles: Array[GH_CssStyle]) -> str
        """
        pass

    def ToString(self):
        """ ToString(self: GH_HtmlWriter) -> str """
        pass

    def WriteBlankSpace(self, height):
        """ WriteBlankSpace(self: GH_HtmlWriter, height: int) """
        pass

    def WriteComment(self, comment):
        """ WriteComment(self: GH_HtmlWriter, comment: str) """
        pass

    def WriteDivEnd(self):
        """ WriteDivEnd(self: GH_HtmlWriter) """
        pass

    def WriteDivStart(self, cssClasses=None):
        """ WriteDivStart(self: GH_HtmlWriter, *cssClasses: Array[GH_CssStyle])WriteDivStart(self: GH_HtmlWriter, *cssClasses: Array[str])WriteDivStart(self: GH_HtmlWriter) """
        pass

    def WriteHorizontalGradient(self, top, bottom, steps, stepHeight):
        """ WriteHorizontalGradient(self: GH_HtmlWriter, top: Color, bottom: Color, steps: int, stepHeight: int) """
        pass

    def WriteHorizontalRule(self, cssClasses=None):
        """ WriteHorizontalRule(self: GH_HtmlWriter, *cssClasses: Array[GH_CssStyle])WriteHorizontalRule(self: GH_HtmlWriter, *cssClasses: Array[str])WriteHorizontalRule(self: GH_HtmlWriter) """
        pass

    def WriteLineBreak(self):
        """ WriteLineBreak(self: GH_HtmlWriter) """
        pass

    def WriteLink(self, target, name, cssClasses=None):
        """ WriteLink(self: GH_HtmlWriter, target: str, name: str, *cssClasses: Array[GH_CssStyle])WriteLink(self: GH_HtmlWriter, target: str, name: str, *cssClasses: Array[str])WriteLink(self: GH_HtmlWriter, target: str, name: str) """
        pass

    def WriteListEnd(self):
        """ WriteListEnd(self: GH_HtmlWriter) """
        pass

    def WriteListItem(self, itemContent, cssClasses=None):
        """ WriteListItem(self: GH_HtmlWriter, itemContent: str, *cssClasses: Array[GH_CssStyle])WriteListItem(self: GH_HtmlWriter, itemContent: str, *cssClasses: Array[str])WriteListItem(self: GH_HtmlWriter, itemContent: str) """
        pass

    def WriteListItemEnd(self):
        """ WriteListItemEnd(self: GH_HtmlWriter) """
        pass

    def WriteListItemStart(self, cssClasses=None):
        """ WriteListItemStart(self: GH_HtmlWriter, *cssClasses: Array[GH_CssStyle])WriteListItemStart(self: GH_HtmlWriter, *cssClasses: Array[str])WriteListItemStart(self: GH_HtmlWriter) """
        pass

    def WriteOrderedListStart(self, start, cssClasses=None):
        """ WriteOrderedListStart(self: GH_HtmlWriter, start: int, *cssClasses: Array[GH_CssStyle])WriteOrderedListStart(self: GH_HtmlWriter, start: int, *cssClasses: Array[str])WriteOrderedListStart(self: GH_HtmlWriter, start: int) """
        pass

    def WritePreEnd(self):
        """ WritePreEnd(self: GH_HtmlWriter) """
        pass

    def WritePreStart(self, cssClasses=None):
        """ WritePreStart(self: GH_HtmlWriter, *cssClasses: Array[GH_CssStyle])WritePreStart(self: GH_HtmlWriter, *cssClasses: Array[str])WritePreStart(self: GH_HtmlWriter) """
        pass

    def WriteSpanEnd(self):
        """ WriteSpanEnd(self: GH_HtmlWriter) """
        pass

    def WriteSpanStart(self, cssClasses=None):
        """ WriteSpanStart(self: GH_HtmlWriter, *cssClasses: Array[GH_CssStyle])WriteSpanStart(self: GH_HtmlWriter, *cssClasses: Array[str])WriteSpanStart(self: GH_HtmlWriter) """
        pass

    def WriteText(self, text, *__args):
        """ WriteText(self: GH_HtmlWriter, text: str, *cssClasses: Array[str])WriteText(self: GH_HtmlWriter, text: str, *cssClasses: Array[GH_CssStyle])WriteText(self: GH_HtmlWriter, text: str)WriteText(self: GH_HtmlWriter, text: str, properties: GH_HtmlTextProperties) """
        pass

    def WriteUnorderedListStart(self, cssClasses=None):
        """ WriteUnorderedListStart(self: GH_HtmlWriter, *cssClasses: Array[GH_CssStyle])WriteUnorderedListStart(self: GH_HtmlWriter, *cssClasses: Array[str])WriteUnorderedListStart(self: GH_HtmlWriter) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cssStyles=None):
        """
        __new__(cls: type)
        __new__(cls: type, *cssStyles: Array[GH_CssStyle])
        """
        pass

    CssStyleSheet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CssStyleSheet(self: GH_HtmlWriter) -> GH_CssStyleSheet

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: GH_HtmlWriter) -> str

Set: Title(self: GH_HtmlWriter) = value
"""



